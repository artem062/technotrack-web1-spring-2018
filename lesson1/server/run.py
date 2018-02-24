# -*- coding: utf-8 -*-
import socket
import os

def get_response(request):

    i = request.find('GET') + 5 
    j = request.find(' ', i)
    url = request[i: j]     # нашли строку с параметрами запроса
    code = request[j + 1: request.find('\r', j + 1)] + ' ' # первая строка http-ответа с кодом ответа
    answer = 'Server: MyPC\nContent-Type: text/html\nConnection: keep-alive\nContent-Length: ' # остальной ответ до текста
    if url == '':
        i = request.find('User-Agent: ') + 12
        code = code + '200 OK\n'
        u = 'Hello mister!<br>You are: ' + request[i: request.find('\n', i + 1)]
    elif url == 'test/' or url == 'test':
        code = code + '\n'
        u = request.replace('\n', '<br>')
    elif url == 'media/' or url == 'media':
        u = ''		
        for x in os.listdir('./files'): u = u + x + '<br>'
        code = code + '200 OK\n'
    elif url.find('media/') == 0:
        try:
            file = open('./files/' + url[6:], "rU")
            code = code + '200 OK\n'
            u = ''
            for line in file.xreadlines():
                u = u + line + '<br>'
        except IOError:
            code = code + '404 Not found\n'
            u = 'File not found'
    else:
        code = code + '404 Not found\n'
        u = 'Page not found'
    return code + answer + str(len(u)) + '\n\n' + u


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  # открываем socket с данным адресом и данным портом
server_socket.listen(0)  # запускаем режим прослущивания соединения

print 'Started'

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  # сигнализируем в консоль о подключении
        request_string = client_socket.recv(2048)  # считываем данные http-запроса
        client_socket.send(get_response(request_string))  # посылаем http-ответ обратно
        client_socket.close()
    except KeyboardInterrupt:  # если введена комбинация Ctrl+C
        print 'Stopped'
        server_socket.close()  # закрываем соединение
        exit()
