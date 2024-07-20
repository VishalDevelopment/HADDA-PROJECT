from flask import Flask , request,jsonify,json
from AllApis.tables import createTables
from AllApis.Users.createUser import createUser
from AllApis.Users.getSpecificUser import getUserData
from AllApis.Users.getUserId import get_user_id_by_credentials
from AllApis.Users.GetAllUser import GetAllUser
from AllApis.Products.addProduct import AddProduct
from AllApis.Products.getAllProducts import getAllProducts

from AllApis.Orders.insertOrder import insertOrder
from AllApis.Orders.getAllOrders import getAllOrdersitem
from AllApis.Orders.getSpecificOrder import getOrdersByUserId,OrderbyOrderId
from AllApis.Orders.orderStatusUpdate import orderstatusUpdate
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
        return jsonify({'success':400,'message':"Email already in Use"})
    

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
     unit = request.form['unit']
     price = request.form['price']
     address=request.form['address']
     check = insertOrder(userId,name,email,phoneNo,category,unit,price,address)
     if check == True:
        return jsonify({'success':200,'message':"Successfully Ordered Items"})
     else:
        return jsonify({'success':400,'message':"Failed to order"})
     

@app.route('/getAllOrder',methods=['GET'])
def getAllOrder():
    return getAllOrdersitem()




@app.route('/orders',methods=['POST'])
def get_orders_by_user_id():
    user_id = request.form['user_id']
    orders = getOrdersByUserId(user_id)
    if orders :
        return json.dumps(orders)
    else:
        return json.dumps(orders)
    

@app.route('/AllUser',methods=['GET'])
def AllUser():
    return GetAllUser()

@app.route('/SpecificOrder',methods=['POST'])
def get_specific_order ():
    id = request.form['orderId']
    specificOrder = OrderbyOrderId(id)
    return specificOrder

@app.route('/UpdateStatus',methods=['POST'])
def statusUpdatewithOrderId():
    orderId = request.form['orderId']
    weight = request.form['weight']
    price = request.form['price']
    status = request.form['status']

    try:
        orderstatusUpdate(orderId,weight,price,status)
        return jsonify({'message' : 'Order Status Updated !!', 'status' : 200}), 200
    except Exception as error:
        return jsonify ({'message' : "Order Status Couldn't Update !!",'status' :400, 'Exception' : str(error)})

if __name__ == "__main__":
    createTables()
    app.run()
    