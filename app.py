from flask import Flask,jsonify
app=Flask(__name__)
@app.route('/test',methods=['POST','GET'])
def test():
    return jsonify({'response':"hello first deva rushi"})
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)