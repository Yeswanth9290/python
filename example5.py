#Rename key of a dictionary

sample_dict={
    "name":"kelly",
    "age":25,
    "salary":8000,
    "city":"newyork"
    }


sample_dict['location']=sample_dict.pop('city')
print(sample_dict)
