for f in ./src/static/md/*.md
do
  STUB=$(echo $f | \
         sed s/".\/src\/static\/md\/"/''/g | \
         sed s/".md"/''/g);
  OUT_PATH=./src/templates/$STUB.html
  PAGE_BODY=$(pandoc -t html $f);
  rm $OUT_PATH;
  echo \
"""
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Jonne Saleva</title>
  <style type="text/css">code{white-space: pre;}</style>
  <link rel="stylesheet" href="../static/css/style.css" type="text/css" />
</head>
""" >> $OUT_PATH;
  echo "<body>" >> $OUT_PATH;
  echo $PAGE_BODY >> $OUT_PATH;
  echo \
"""
</body>
</html>
""" >> $OUT_PATH;
done
