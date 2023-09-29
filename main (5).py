# 3.1

def linearSearchProductList,targetProduct):
for index,product in enumerate(productList):
  if product==targetProduct:
    indices.append(index)
    return indices
# Example usage:
products=["shoes","boot","loafer","shoes","sandal","shoes"]
target="shoes"
target="apple"
result=linearSearchProduct(products,target)
print(result)