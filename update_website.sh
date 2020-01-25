./markdown_to_html.sh;
git add --all;
git commit -m "$1";
git pull origin;
git push origin;
