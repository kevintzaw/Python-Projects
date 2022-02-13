f = open("demofile2.html", "a")

#entering text
enterText = input("Enter your text: ")

#outputs text
f.write('\
<html> \
<body> \
<p id="demo"></p>\
<script>\
function myFunction() { \
    var x = document.getElementById("enterText");\
    document.getElementById("demo").innerHTML = x;\
}\
</script>\
</body> \
</html>')
f.close()

#open and read the file after the appending:
f = open("demofile2.html", "r")
print(f.read())
