from collections import defaultdict
import src.helpers as h
import pypandoc
import os

class Blog:
    def __init__(self, blog_path='blog', extension='.md'):
        self.extension = extension
        self.blog_path = os.path.abspath(blog_path)
        self.posts = self.load_posts()

    def load_posts(self):
        posts = {}
        for f in os.listdir(self.blog_path):
            print('f = {}'.format(f))
            if f.endswith(f".{self.extension}"):
                print(f"{f} doesn't end with '{self.extension}'")
                print('skipping...')
                continue
            path = f"{self.blog_path}/{f}"
            post = BlogPost(path)
            posts[f] = post

        print('found the following posts')
        print(posts)
        return posts

    def __getitem__(self, identifier):
        return self.posts[identifier]

    def __setitem__(self, identifier):
        # this is correct -- we want read only!
        raise NotImplementedError

class BlogPost:

    def __init__(self, fp):
        with open(fp, 'r') as f:
            blog_post_content = f.read()
            metadata, post = self.process(blog_post_content)
            self.metadata = metadata
            self.post = post

    def process(self, post):
        header_end_ix = h.find_last(h.HEADER_PATTERN, post)
        post_start_ix = header_end_ix + len(h.HEADER_PATTERN)
        header, post = h.split_at_ix(post, post_start_ix)
        header_info = self.parse_header(header)
        post = pypandoc\
                .convert_text(post, to='html', format='markdown')\
                .replace('&lt;', '<')\
                .replace('&gt;', '>')

        return header_info, post

    def parse_header(self, header):
        header = header.replace(h.HEADER_PATTERN, '')
        header_info = {}
        for row in header.split('\n'):
            try:
                k, v = [s.strip() for s in row.split(':')]
                header_info[k] = v
            except:
                continue
        return header_info
