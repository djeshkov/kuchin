CTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <script type="application/javascript" src="http://d3js.org/d3.v3.min.js"></script>
  </head>
  <body>
    <script type="application/javascript">
      d3.select('body').selectAll('p')
        .data([16, 23, 42])
        .enter()
        .append('p')
        .text("Hello");
    </script>
  </body>
</html>

