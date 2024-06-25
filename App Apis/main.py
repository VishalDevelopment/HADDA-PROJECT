from flask import Flask , request,jsonify
from AllApis.tables import createTables
from AllApis.Users.createUser import createUser
from AllApis.Users.getSpecificUser import getUserData
from AllApis.Users.getUserId import get_user_id_by_credentials
from AllApis.Products.addProduct import AddProduct
from AllApis.Products.getAllProducts import getAllProducts

from AllApis.Orders.insertOrder import insertOrder
app = Flask(__name__)
@app.route("/")

def Home():
    return "Api is Working..."

@app.route("/createUser",methods = ['POST'])
def CreateUser():
    name = request.form['name']
    email = request.form['email']
    phone_no = request.form['phoneNo']
    address = request.form['address']
    password = request.form['password']
    check = createUser(name,email,phone_no,address,password)
    if check == True:
        return jsonify({'success':200,'message':"Successfully Sign Up"})
    else:
        return jsonify({'success':400,'message':"Failed Sign Up"})
    

@app.route("/GetUser",methods = ['POST'])
def getUser():
   userId = request.form['userId']
   return getUserData(userId)
   
   
@app.route("/AddProduct",methods =['POST'])
def addProduct():
   category = request.form['category']
   price = request.form['price']
   status = request.form['status']
   unit = int(request.form['unit'])
   check = AddProduct(category,price,status,unit)
   if check == True:
    return jsonify({'success':200,'message':"Product Added Succesfully"})
   else:
        return jsonify({'success':400,'message':"Product Add to Failed"})
   
@app.route('/loginUser', methods = ['POST'])
def loginUser():
        email= request.form['email']
        password = request.form['password']
       
        dbRes= get_user_id_by_credentials(email , password)
        if dbRes:  
         return jsonify({'success':200,"message": dbRes})
        else:
         return jsonify({'success':400,"message":"unable to find ID"}) 
        
@app.route('/getAllProduct',methods =['GET'])
def allProducts():
    return getAllProducts()

@app.route('/OrderItems',methods=['POST'])
def orderItem():
     userId =request.form['userID']
     name = request.form['name']
     email = request.form['email']
     phoneNo = request.form['phoneNo']
     category = request.form['category']
     price = request.form['price']
     address=request.form['address']
     check = insertOrder(userId,name,email,phoneNo,category,price,address)
     if check == True:
        return jsonify({'success':200,'message':"Successfully Ordered Items"})
     else:
        return jsonify({'success':400,'message':"Failed to order"})


if __name__ == "__main__":
    createTables()
    app.run()
    