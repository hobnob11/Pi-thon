import httplib
print(httplib.HTTPConnection("freedns.afraid.org",80).request("GET","/dynamic/update.php?YTVEWUpTcmdvTFFKVzdwRE1zbG5rb1RlOjE1MjEyMDYw").getresponce().read())
