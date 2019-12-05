import pandas as pd 
import xml.etree.ElementTree as ET
from sqlalchemy import create_engine
import csv
import backend

engine=create_engine('postgresql://postgres:postgres1984@localhost:5432/postgres')
conn=engine.connect()
tree=ET.parse('newfile.xml')
#print(type(tree))
root=tree.getroot()
print(root)

df_columns=["product-id","online-from","online-to","amount","price-info"]
df_rows=[]
#for x in root.findall('./pricebook/price-tables/price-table'):
for x in root.findall('price-table'):
    #print(x)
    product_id=x.attrib.get('product-id')
    online=x.find('online-from').text
    online_to=x.find('online-to').text
    amount=x.find('amount').text
    price=x.find('price-info').text
    print(product_id,online,online_to,amount,price)

    df_rows.append({"product-id":product_id,"online-from":online,"online-to":online_to,"amount":amount,"price-info":price})
    output=pd.DataFrame(df_rows,columns=df_columns)
    
    
    #print(output)

    output.rename(columns={'product-id':'productid',
                         'online-from':'onlinefrom',
                          'online-to':'onlineto',
                          'price-info':'priceinfo'}, 
                 inplace=True)
    
    #output.to_csv(r'C:\Users\Sravani\Desktop\productsdata.csv',index=False,header=True) 
    
    
    #print(output.info())
#print(output.describe())


    output.to_sql('importeddata',con=engine,if_exists='replace',index=False)
    
    
    conn.close()