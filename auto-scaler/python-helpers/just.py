import os

print(os.getcwd()+"/jajsj")

a = ["dw", "dskd"]
b = "jis"

print(a + [b])
my_dict = {'requests': 1682.0, 'throughput': 0, 'mean': 544.6213942307693, 'std_dev': 44.87185076476029, '99per': 623.046875}
values = list(my_dict.values())
print(type(values))
print(values + ["hdhdh"])

ip_address = "10.32.1.23"
URL = "http://"+ip_address+":9797/metrics"
print(URL)

li = ['sdasd','kosw']
print(tuple(li))

arr = [[1,2],[7,8]]
array = arr[:]
array[0][1] = 5
print(array)