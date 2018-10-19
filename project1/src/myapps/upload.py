import base64
import sys
from jsonrpc.proxy import ServiceProxy

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage {} <file> <category_id>".format(sys.argv[0])
        sys.exit(1)

    file_name = sys.argv[1]
    category_id = sys.argv[2]
    rpc_server = ServiceProxy('http://127.0.0.1:8000/api/')
    with open(file_name, 'rb') as input_content:
        content = base64.b64encode(input_content.read())
        response = rpc_server.api.upload_file(content.decode('utf8'), file_name, category_id)
        print response
    # response = rpc_server.api.question_detail();
    # print response
