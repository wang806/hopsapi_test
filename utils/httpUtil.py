from utils.logger import Log
from utils import getParams
import configparser as cparser
import requests
import json
import os
import ssl
from urllib import parse
logger = Log(logger='HttpUtil').get_log()

# 读取配置
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + '/config.ini'
cf = cparser.ConfigParser()
cf.read(file_path, encoding='utf-8')

# 指定files目录,存放下载的文件
report_path = base_dir.split('utils')[0]
file_path = os.path.join(report_path, 'report/files/')
if not os.path.exists(file_path):
    os.mkdir(file_path)


class HttpUtil:
    accessToken = ''

    def __init__(self):
        ssl._create_default_https_context = ssl._create_default_https_context
        self.headers = {'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json;charset=UTF-8',
                        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0',
                        'Authorization': self.accessToken, 'Connection': 'close'}
        print(self.headers)
        self.base_url = cf.get('URL', 'base_url')
        self.sso_url = cf.get('URL', 'sso_url')
        self.port = cf.get('URL', 'port')
        if self.port:
            self.url = "https://" + self.base_url + ":" + self.port
            self.sso_url = "https://" + self.sso_url + ":" + self.port
        else:
            self.url = "https://" + self.base_url
            self.sso_url = "https://" + self.sso_url

    @classmethod
    def get_token(cls):
        path = getParams.get_url('cms_login', 'login_Sucess')
        # params = getParams.get_req_params('cms_login', 'login_Sucess')
        params = getParams.get_params('cms_login', 'login_Sucess')
        response = cls().do_post(path, params)
        # 登录sso,获取sso返回的token
        accessToken = response['data']['token']
        applicationToken = response['data']['applicationToken']
        # 调用sso checkToken接口校验token有效性
        c_path = '/api/checkToken'
        c_params = dict()
        c_params['token'] = accessToken
        c_params['appFlag'] = ''
        c_params['applicationToken'] = applicationToken
        logger.info('c_params: %s' % c_params)
        c_response = cls().do_post(c_path, c_params)
        logger.info('c_response: %s' % c_response)
        # 调用sso selectTenant接口,获取applicationToken
        selectTenant_path = '/api/selectTenant'
        selectTenant_params = dict()
        selectTenant_params['accessToken'] = ''
        selectTenant_params['loginToken'] = accessToken
        selectTenant_params['tenantId'] = 6
        selectTenant_response = cls().do_post(selectTenant_path, selectTenant_params)
        cls.accessToken = selectTenant_response['data']['token']

    def do_get(self, path):
        url = self.url + path
        logger.info('>>>request url is: %s' % url)
        try:
            r = requests.get(url=url, headers=self.headers)
            logger.info('>>>header: %s' % self.headers)
            r.encoding = 'UTF-8'
            json_response = r.json()
            logger.info('>>>response: %s' % json_response)
            return json_response
        except Exception as e:
            return {'code': 1, 'result': 'get请求出错，出错原因:%s' % e}

    def do_get_with_params(self, path, params):
        url = self.url + path
        logger.info('>>>request url is: %s?%s' % (url, params))
        try:
            r = requests.get(url=url, params=params, headers=self.headers)
            r.encoding = 'UTF-8'
            json_response = r.json()
            logger.info('>>>response: %s' % json_response)
            if 200 == r.status_code:
                return json_response
        except Exception as e:
            logger.info(e)
            return {'code': 1, 'result': 'get请求出错，出错原因:%s' % e}

    def do_download_file(self, path, params):
        url = self.url + path
        logger.info('>>>request url is: %s?%s' % (url, params))
        try:
            r = requests.get(url=url, params=params, headers=self.headers)
            # 从Response Headers - Content-disposition中获取文件名并解析
            file_name = parse.unquote(r.headers['Content-disposition'].split('filename=')[-1])
            print(file_name)
            # 指定下载文件存放路径并写入文件内容
            file = file_path + file_name
            if 200 == r.status_code:
                with open(file, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1):
                        f.write(chunk)
                return r
        except Exception as e:
            logger.info(e)
            return {'code': 1, 'result': 'get请求出错，出错原因:%s' % e}

    def do_post(self, path, params):
        if path == '/api/login' or path == '/api/checkToken' or path == '/api/selectTenant':
            url = self.sso_url + path
            self.headers = {'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json;charset=UTF-8',
                        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0', 'Connection': 'close'}
        else:
            url = self.url + path
        logger.info('>>>request url %s' % url)
        params = json.dumps(params)
        logger.info('>>>params %s' % params)
        try:
            s = requests.session()
            s.keep_alive = False
            r = requests.post(url=url, data=params, headers=self.headers)
            json_response = r.json()
            logger.info('>>>response: %s' % json_response)
            if 200 == r.status_code:
                return json_response
        except Exception as e:
            logger.error(e)
            return {'code': 1, 'result': 'post请求出错，出错原因: %s' % e}

    def del_file(self, path, params):
        url = self.url + path
        try:
            del_word = requests.delete(url=url, data=params, headers=self.headers)
            json_response = del_word.json()
            return {'code': 0, 'result': json_response}
        except Exception as e:
            return {'code': 1, 'result': 'del请求出错，出错原因:%s' % e}

    def put_file(self, path, params):
        url = self.url + path
        try:
            params = json.dumps(params)
            me = requests.put(url=url, data=params)
            json_response = me.json()
            return {'code': 0, 'result': json_response}
        except Exception as e:
            return {'code': 1, 'result': 'put请求出错，出错原因:%s' % e}
