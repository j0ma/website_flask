import pypandoc
import os

HEADER_PATTERN='---'

def load_blog_post(identifier, blog_path):
    with open(f'{blog_path}/{identifier}.md', 'r') as f:
        blog_post_content = f.read()
        header_info, post = process_blog_post(blog_post_content)
        title = header_info['title']

    return title, post

def load_blog_posts(blog_path):
    posts = [f.replace('.md', '') 
             for f in os.listdir(blog_path) 
             if f.endswith('md')]
    posts = sorted(posts)
    return posts

def find_all(pattern, text, start_ix=0):
    """
    Finds all starting indices of `pattern` inside `text`
    """
    first_ix = text.find(pattern)
    if first_ix == -1:
        return []
    else:
        start_ix = start_ix + first_ix
        end_ix = start_ix + len(pattern)
        rest = text[first_ix+len(pattern):]
        return [start_ix] + find_all(pattern, rest, 
                                     start_ix=end_ix)

def find_last(pattern, text):
    try:
        return find_all(pattern, text)[-1]
    except:
        return None

def split_at_ix(text, ix):
    return text[:ix], text[ix:]

def parse_header(header):
    header = header.replace(HEADER_PATTERN, '')
    header_info = {}
    for row in header.split('\n'):
        try:
            k, v = [s.strip() for s in row.split(':')]
            header_info[k] = v
        except:
            continue
    return header_info

def process_blog_post(post):
    header_end_ix = find_last(HEADER_PATTERN, post)
    post_start_ix = header_end_ix + len(HEADER_PATTERN)
    header, post = split_at_ix(post, post_start_ix)
    header_info = parse_header(header)
    #post = post.strip()
    post = pypandoc\
            .convert_text(post, to='html', format='markdown')\
            .replace('&lt;', '<')\
            .replace('&gt;', '>')

    return header_info, post

