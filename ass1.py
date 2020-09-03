#!/usr/bin/env python
# coding: utf-8

# # LIST

# In[16]:


lst = ["Aparna",20,1701230041,123.45,[1,2,3]]


# In[17]:


lst


# In[18]:


lst[2]


# In[19]:


lst.append("ram")    #it will add a element at the end


# In[20]:


lst


# In[21]:


lst1 =["Aparna",10]


# In[23]:


lst1


# In[24]:


lst1.clear()  # it will remove all the item from the list


# In[25]:


lst1


# In[26]:


lst.copy()   # it will copy all the element present in the previous list


# In[27]:


lst1.copy()


# In[30]:


lst.count("Aparna")   #it will return the count of a given element in a list


# In[32]:


lst.extend("Alok")


# In[33]:


lst


# In[35]:


lst.index(20)


# In[36]:


lst.index(1701230041)


# In[45]:


lst.insert(0,1)


# In[46]:


lst


# In[48]:


lst.remove("Ayush")


# In[49]:


lst


# In[50]:


lst.remove(1)


# In[51]:


lst


# In[52]:


lst.remove(2)


# In[53]:


lst


# In[54]:


lst.reverse()


# In[55]:


lst


# In[56]:


lst.pop()


# lst.sort()   # Sir here it show error why 

# In[69]:


lst.sort()


# In[70]:


print ("List now  :", lst)


# # Dictionary

# In[113]:


dit = {"name":"Aparna","Age":19,"phone no":7633837033,"email id":"aparnanibha@gmail.com"}


# In[114]:


dit


# In[115]:


dit.get("name")


# In[116]:


dit1 = {"name":"aparna","roll no":8}


# In[117]:


dit1


# In[118]:


dit1.clear()


# In[119]:


dit1


# In[120]:


dit.copy()


# In[121]:


dit.items()


# In[122]:


dit


# In[123]:


dit.get("name")


# In[124]:


dit.fromkeys("name","Aparna")


# In[125]:


dit.keys()


# In[92]:


dit.pop("name")


# In[127]:


dit.pop("name")


# In[128]:


dit.popitem()


# In[129]:


dit.update(dit1)


# In[130]:


dit


# In[103]:


dit1


# In[131]:


dit


# In[132]:


dit.values()


# In[139]:


dit.setdefault("name")


# In[142]:


dit


# # SETS

# In[146]:


st= {"aparna","aparnanibha@gmail.com",1701230041,"aparna"}


# In[147]:


st


# In[148]:


st1={"aparna",1701230041}


# In[151]:


st1.issubset(st)


# In[152]:


st.add("adarsh vidya mandir")


# In[153]:


st


# In[154]:


st1.clear()


# In[155]:


st1


# In[156]:


st.remove("adarsh vidya mandir")


# In[157]:


st


# In[162]:


st2 = {"aparna",19}


# In[163]:


st2


# In[164]:


st.union(st2)


# # TUPLE

# In[165]:


tup = ("Ayush","Ranjan",1701230042,"@")


# In[166]:


tup


# In[167]:


tup.count("Ayush")


# In[168]:


tup.index(1701230042)


# In[169]:


tup.index("@")


# # STRING

# In[170]:


print("Hello World")


# In[171]:


a= "Aparna"


# In[172]:


print(a)


# In[173]:


a=""" My name is Aparna. I enroll in Letsupgrade for learning python or basically to build a project.
Here i get SAI sir as my instructor and he is awesome,his way of teaching is very impressive or interactive
but he is so fast  hahahah , it may be due to less time."""


# In[174]:


print(a)


# In[175]:


a="Hello, World"


# In[176]:


print(a[1])


# In[177]:


print(a[2:5])


# In[178]:


print(a[-5:-2])


# In[179]:


print(len(a))


# In[180]:


print(a.strip())


# In[181]:


print(a.lower())


# In[182]:


print(a.upper())


# In[183]:


print(a.replace("H","J"))


# In[ ]:




