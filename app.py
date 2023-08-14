from flask import Flask, jsonify, request

#jsonify es para que nos responda por medio del formato json
#app es la aplicacion del sevidor pero toca iniciarlo por medio de una condicional

app = Flask(__name__)

from products import products


'''Testing Route o ruta de prueba para que el sevidor responda con algo y 
se ejecute para que  responda con un json en este caso la respuesta al buscar  http://127.0.0.1:5000/ping 
la respuesta sera  response": "pong en fomato json  y esto se le llama un texteo '''

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})


'''Una ruta por defecto siempre usa el Get entonces toca especificar el metodo sea get post o etc '''


# Get Data Routes
@app.route('/products')
def getProducts():
    # return jsonify(products)
    return jsonify({'products': products})


'''al buscar http://127.0.0.1:5000/products nos va ha mostrar con una lista de todos los productos '''



@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [
        product for product in products if product['name'] == product_name.lower()]
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
    return jsonify({'message': 'Product Not found'})


'''En este caso cuando añadimos desde el navegador  otra ruta para que cuando se busque
algo en especifico en este caso name utilizando como id el nombre de cada producto por medio de un string
y que por medio del areglo el queremos obtener un solo producto asi que se recorre cada uno de los
productos mediante un for y cree una condicion en su propiedad name es igual al product name guarde ese
valor y lo retorne como un json una lista el producto encontrado o el valo 0 y si no lo encontro aparezca
un json con el mensaje Product Not found '''


# Create Data Routes
@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': 10
    }
    products.append(new_product)
    return jsonify({'products': products})


'''En este caso utilizamos un metodo diferente  va a ser un Post para enviar informacion y aunque tengan
  la misma ruta tiene diferente metodo ahora esto sirve para enviar datos nuevos datos al servidor y para eso 
  usamos el request para imprimir solo los datos que son tipo json y toca guardar estos datso en una nueva variable 
  new_producto   y nos va a mostrar por medio de  products.append(new_product) y nos retorna 
  return jsonify({'products': products}) que es igual a profuctos agregados correctamente '''

# Update Data Route
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'product'oductsFound[0]: pr
        })
    return jsonify({'message': 'Product Not found'})

''' El metodo Put es para recibir un producto en especifico y actualizarlo y aunque usamos la misma ruta el metodo cambia
por medio de una funcion llamada editproduct
y en este caso si el producto se encuentra va a ser editado y en este caso seleccionamos una 
propiedad puede ser tanto name como price o quiantity para editar los datos principales y
utulizamos el retun para que nos regrese los productos actualizados y si no se encuentra nos va a devolver
un json con el mensaje 
return jsonify({'message': 'Product Not found'})'''

# DELETE Data Route
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': products
        })
        
'''Ahora cramos una ruta para eliminar mediante el metodo delete mendiante una funcion llamada deleteproducto
 y si un producto coincide con el parametro enviado y retornamos un json con el mensaje producto elimnado '''

if __name__ == '__main__':
    app.run(debug=True, port=4000)