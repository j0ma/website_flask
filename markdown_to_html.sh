# iterate over .md files in /src/static/md
for f in ./src/static/md/*.md
do
  # grab stub, i.e. name of file without path or extension
  STUB=$(echo $f | \
         sed s/".\/src\/static\/md\/"/''/g | \
         sed s/".md"/''/g);

  # compose path to output HTML file using the stub
  OUT_PATH=./src/templates/$STUB.html

  # convert the .md file to html and store the body in a variable
  PAGE_BODY=$(pandoc -t html $f);

  # remove old version of output HTML file
  rm $OUT_PATH;

  ## CREATING NEW HTML FILE ##

  # append header of HTML page to output file
  echo \
"""
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Jonne Sälevä</title>
  <style type="text/css">code{white-space: pre;}</style>
  <link rel="stylesheet" href="../static/css/style.css" type="text/css" />
</head>
""" >> $OUT_PATH;

  # create body of output HTML document and append it to output file
  echo "<body>" >> $OUT_PATH;
  echo $PAGE_BODY >> $OUT_PATH;

  # finally close out the <body> and <html> tags
  echo \
"""
</body>
</html>
""" >> $OUT_PATH;
done
