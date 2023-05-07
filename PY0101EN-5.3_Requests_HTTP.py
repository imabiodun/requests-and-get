#!/usr/bin/env python
# coding: utf-8

# <a href="https://cognitiveclass.ai/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork1005-2022-01-01">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png"                        width="300" align="center">
# </a>
# 

# <h1> HTTP and Requests</h1>
# 
# Estimated time needed: **15** minutes
#     
# 
# ## Objectives
# 
# After completing this lab you will be able to:
# 
# * Understand HTTP    
# * Handle HTTP Requests
# 

# <h2>Table of Contents</h2>
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <ul>
#         <li>
#             <a href="#index">Overview of HTTP </a>
#             <ul>
#                 <li><a href="#HTTP">Uniform Resource Locator:URL</a></li>
#                  <li><a href="slice">Request</a></li>
#                 <li><a href="stride">Response</a></li>
#             </ul>
#         </li>
#         <li>
#             <a href="#RP">Requests in Python  </a>
#             <ul>
#                 <li><a href="#get">Get Request with URL Parameters</a></li>
#                 <li><a href="#post">Post Requests </a></li>
# 
# </ul>
#     
# </div>
# 
# <hr>
# 

# <h2 id="">Overview of HTTP </h2>
# 

# When you, the **client**, use a web page your browser sends an **HTTP** request to the **server** where the page is hosted. The server tries to find the desired **resource** by default "<code>index.html</code>". If your request is successful, the server will send the object to the client in an **HTTP response**. This includes information like the type of the **resource**, the length of the **resource**, and other information.   
# <p>
# The figure below represents the process. The circle on the left represents the client, the circle on the right represents the Web server. The table under the Web server represents a list of resources stored in the web server. In  this case an <code>HTML</code> file, <code>png</code> image, and <code>txt</code> file .
# </p>
# <p>
# The <b>HTTP</b> protocol allows you to send and receive information through the web including webpages, images, and other web resources. In this lab, we will provide an overview of the Requests library for interacting with the <code>HTTP</code> protocol. 
# </p
# 

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/reqest_basics.png" width="750" align="center">
#    
# </div>
# 

# <h2 id="URL">Uniform Resource Locator: URL</h2>
# 

# Uniform resource locator (URL) is the most popular way to find resources on the web.  We can break the URL into three parts. 
# <ul>
#     <li><b>scheme</b> this is this protocol, for this lab it will always be <code>http://</code>  </li>
#     <li><b> Internet address or  Base URL </b> this will be used to find the location here are some examples: <code>www.ibm.com</code> and  <code> www.gitlab.com </code> </li>
#     <li><b>route</b> location on the web server for example: <code>/images/IDSNlogo.png</code> </li>
# </ul>
# 

# You may also hear the term Uniform Resource Identifier (URI), URL are actually a subset of URIs. Another popular term is endpoint, this is the URL of an operation provided by a Web server.
# 

# <h2 id="RE">Request </h2>
# 

# The process can be broken into the <b>request</b> and <b>response </b> process.  The request using the get method is partially illustrated below. In the start line we have the <code>GET</code> method, this is an <code>HTTP</code> method. Also the location of the resource  <code>/index.html</code> and the <code>HTTP</code> version. The Request header passes additional information with an <code>HTTP</code> request:
# 

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/reqest_messege.png" width="400" align="center">
# </div>
# 

# When an <code>HTTP</code> request is made, an <code>HTTP</code> method is sent, this tells the server what action to perform.  A list of several <code>HTTP</code> methods is shown below. We will go over more examples later.
# 

# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/http_methods.png" width="400" align="center">
# </div>
# 

# <h2 id="RES">Response</h2>
# 

# The figure below represents the response; the response start line contains the version number <code>HTTP/1.0</code>, a status code (200) meaning success, followed by a descriptive phrase (OK). The response header contains useful information. Finally, we have the response body containing the requested file, an <code> HTML </code> document.  It should be noted that some requests have headers.
# 

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/response_message.png" width="400" align="center">
# </div>
# 

# Some status code examples are shown in the table below, the prefix indicates the class. These are shown in yellow, with actual status codes shown in  white. Check out the following <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Status?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork1005-2022-01-01">link </a> for more descriptions.
# 

# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/status_code.png" width="300" align="center">
# </div>
# 

# <h2 id="RP">Requests in Python</h2>
# 

# Requests is a Python Library that allows you to send <code>HTTP/1.1</code> requests easily. We can import the library as follows:
# 

# In[23]:


import requests


# We will also use the following libraries: 
# 

# In[2]:


import os 
from PIL import Image
from IPython.display import IFrame


#  You can make a <code>GET</code> request via the method <code>get</code> to www.ibm.com: 
# 

# In[48]:


url='https://www.ibm.com/'
r=requests.get(url)


# We have the response object <code>r</code>, this has information about the request, like the status of the request. We can view the status code using the attribute <code>status_code</code>. 
# 

# In[49]:


r.cookies


# In[50]:


r.status_code


# You can view the request headers:
# 

# In[51]:


print(r.request.headers)


# You can view the request body, in the following line, as there is no body for a get request we get a <code>None</code>:
# 

# In[52]:


print("request body:", r.request.body)


#  You can view the <code>HTTP</code> response header using the attribute <code>headers</code>. This returns a python dictionary of <code>HTTP</code> response headers. 
# 

# In[53]:


header=r.headers
print(r.headers)


# We can obtain the date the request was sent using the key <code>Date</code>
# 

# In[54]:


header['date']


# <code>Content-Type</code> indicates the type of data:
# 

# In[55]:


header['Content-Type']


# You can also check the <code>encoding</code>:
# 

# In[56]:


r.text


# As the <code>Content-Type</code> is <code>text/html</code> we can use the attribute <code>text</code> to display the <code>HTML</code> in the body. We can review the first 100 characters:
# 

# In[57]:


r.text[0:149]


# You can load other types of data for non-text requests, like images. Consider the URL of the following image:
# 

# In[58]:


# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'


# We can make a get request:
# 

# In[59]:


r=requests.get(url)


# We can look at the response header:
# 

# In[60]:


print(r.headers)


# We can see the <code>'Content-Type'</code>
# 

# In[61]:


r.headers['Content-Type']


# An image is a response object that contains the image as a <a href="https://docs.python.org/3/glossary.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork1005-2022-01-01#term-bytes-like-object">bytes-like object</a>. As a result, we must save it using a file object. First, we specify the file path and
# name 
# 

# In[62]:


path=os.path.join(os.getcwd(),'image.png')
path


# We save the file, in order to access the body of the response we use the attribute <code>content</code> then save it using the <code>open</code> function and write <code>method</code>: 
# 

# In[63]:


with open(path,'wb') as f:
    f.write(r.content)


# We can view the image:
# 

# In[64]:


Image.open(path)  


# <h3>Question 1: write <a href="https://www.gnu.org/software/wget/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork1005-2022-01-01"><code> wget </code></a></h3>
# 

# In the previous section, we used the <code>wget</code> function to retrieve content from the web server as shown below.  Write the python code to perform the same task. The code should be the same as the one used to download the image, but the file name should be <code>'Example1.txt'</code>. 
# 

# <code>!wget -O /resources/data/Example1.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt</code>
# 

# In[ ]:





# <details><summary>Click here for the solution</summary>
# 
# ```python
# url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
# path=os.path.join(os.getcwd(),'example1.txt')
# r=requests.get(url)
# with open(path,'wb') as f:
#     f.write(r.content)
# 
# ```
# 
# </details>
#  
# 

# <h2 id="URL_P">Get Request with URL Parameters </h2>
# 

# You can use the <b>GET</b> method to modify the results of your query, for example retrieving data from an API. We send a <b>GET</b> request to the  server. Like before we have the <b>Base URL</b>, in the <b>Route</b> we append <code>/get</code>, this indicates we would like to preform a <code>GET</code> request. This is demonstrated in the following table:
# 

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/base_URL_Route.png" width="400" align="center">
# </div>
# 

# The Base URL is for <code>http://httpbin.org/</code> is a simple HTTP Request & Response Service. The <code>URL</code> in Python is given by:
# 

# In[65]:


url_get='http://httpbin.org/get'


# A <a href="https://en.wikipedia.org/wiki/Query_string?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork1005-2022-01-01">query string</a> is a part of a uniform resource locator (URL), this sends other information to the web server. The start of the query is a <code>?</code>, followed by a series of parameter and value pairs, as shown in the table below. The first parameter name is <code>name</code> and the value is <code>Joseph</code>. The second parameter name is <code>ID</code> and the Value is <code>123</code>. Each pair, parameter, and value is separated by an equals sign, <code>=</code>.
# The series of pairs is separated by the ampersand <code>&</code>.
# 

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#          <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/images/query_string.png" width="500" align="center">
# </div>
# 

# To create a Query string, add a dictionary. The keys are the parameter names and the values are the value of the Query string.
# 

# In[ ]:


payload={"name":"Joseph","ID":"123"}


# Then passing the dictionary <code>payload</code> to the <code>params</code> parameter of the <code> get()</code> function:
# 

# In[ ]:


r=requests.get(url_get,params=payload)


# 
# We can print out the <code>URL</code> and see the name and values 
# 

# In[ ]:


r.url


# There is no request body 
# 

# In[ ]:


print("request body:", r.request.body)


# We can print out the status code
# 

# In[ ]:


print(r.status_code)


# We can view the response as text:
# 

# In[ ]:


print(r.text)


# We can look at the <code>'Content-Type'</code>.
# 

# In[ ]:


r.headers['Content-Type']


# As the content <code>'Content-Type'</code> is in the <code>JSON</code> format we can use the method <code>json()</code>, it returns a Python <code>dict</code>:
# 

# In[ ]:


r.json()


# The key <code>args</code> has the name and values:
# 

# In[ ]:


r.json()['args']


# <h2 id="POST">Post Requests  </h2>
# 

# Like a <code>GET</code> request, a <code>POST</code> is used to send data to a server, but the <code>POST</code> request sends the data in a request body. In order to send the Post Request in Python, in the <code>URL</code> we change the route to <code>POST</code>:
# 

# In[ ]:


url_post='http://httpbin.org/post'


# This endpoint will expect data as a file or as a form. A form is convenient way to configure an HTTP request to send data to a server.
# 

# To make a <code>POST</code> request we use the <code>post()</code> function, the variable <code>payload</code> is passed to the parameter <code> data </code>:
# 

# In[ ]:


r_post=requests.post(url_post,data=payload)


# Comparing the URL from the response object of the <code>GET</code> and <code>POST</code> request we see the <code>POST</code> request has no name or value pairs.
# 

# In[ ]:


print("POST request URL:",r_post.url )
print("GET request URL:",r.url)


# We can compare the <code>POST</code> and <code>GET</code> request body, we see only the <code>POST</code> request has a body:
# 

# In[ ]:


print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)


# We can view the form as well:
# 

# In[ ]:


r_post.json()['form']


# There is a lot more you can do. Check out <a href="https://requests.readthedocs.io/en/master/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork1005-2022-01-01">Requests </a> for more.
# 

# <hr>
# 

# ## Authors
# 
# <p><a href="https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork1005-2022-01-01" target="_blank">Joseph Santarcangelo</a> <br>A Data Scientist at IBM, and holds a PhD in Electrical Engineering. His research focused on using Machine Learning, Signal Processing, and Computer Vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.</p>
# 

# ### Other Contributors 
# 
# <a href="www.linkedin.com/in/jiahui-mavis-zhou-a4537814a">Mavis Zhou</a>
# 

# ## Change Log
# 
# |  Date (YYYY-MM-DD) |  Version | Changed By  |  Change Description |
# |---|---|---|---|
# |2021-12-20 | 2.1 | Malika | Updated the links |
# | 2020-09-02  | 2.0  | Simran | Template updates to the file|
# |   |   |   |   |
# |   |   |   |   |
# 
# 
# 
# 
# ## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>
# 
