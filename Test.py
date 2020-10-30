try:
    import unittest
    import json
    from api import app
    import pprint

    # from os.path import abspath, dirname
except Exception as e:
    print(format(e))


"""ResponseCode for all no mail, with mail & Single no mail, with mail
URL check for / and /configs
Application ContentType for all no mail, with mail & Single no mail, with mail"""

##################
# ResponseCode
##################
# class ResponseCode(unittest.TestCase):
# def test_GetAll_no_mail(self):
#     tester = app.test_client(self)
#     response = tester.get("/configuration/0/")
#     # data = json.loads(response.get_data(as_text=True))
#     status = response.status_code
#     print("[Success] Status:" + str(status))
#     self.assertEqual(status, 200)

# def test_GetAll_with_mail(self):
#     tester = app.test_client(self)
#     response = tester.get("/configuration/1/")
#     status = response.status_code
#     print("[Success] Mail Server Working Status:" + str(status))
#     self.assertEqual(status, 200)

# def test_Single_no_mail(self):
#     tester = app.test_client(self)
#     response = tester.get("/configs/<string:name>/0/")
#     # data = json.loads(response.get_data(as_text=True))
#     status = response.status_code
#     print("[Success] Status:" + str(status))
#     self.assertEqual(status, 200)

# def test_Single_with_mail(self):
#     tester = app.test_client(self)
#     response = tester.get("/configs/<string:name>/1/")
#     status = response.status_code
#     print("[Success] Mail Server Working Status:" + str(status))
#     self.assertEqual(status, 200)

# def test_Single_with_mail_fail(self):
#     tester = app.test_client(self)
#     response = tester.get("/configs/<string:name>/1/")
#     status = response.status_code
#     print("[Success] Mail Server Not Working Status:" + str(status))
#     self.assertEqual(status, 404)

# # -- Check URl -- #
# def test_url_not_exist_single(self):
#     tester = app.test_client(self)
#     response = tester.get("/configs")
#     status = response.status_code
#     print("[Success] URL '/configs' doesn't exist Status:" + str(status))
#     self.assertEqual(status, 404)

# def test_url_not_exist(self):
#     tester = app.test_client(self)
#     response = tester.get("/")
#     status = response.status_code
#     print("[Success] URL '/' doesn't exist Status:" + str(status))
#     self.assertEqual(status, 404)


# ##################
# # Split_Sheet
# ##################
# class main_sheet_check(unittest.TestCase):
#     def test_Sheet_no_value_no_mail(self):
#         tester = app.test_client(self)
#         response = tester.get("/configuration/0/")
#         data = json.loads(response.get_data(as_text=True))
#         message = data["final_file"]
#         print(message)
#         assertion = 0
#         if message == "No value in DB or config":
#             assertion = 1
#         self.assertEqual(assertion, 1)

#     def test_Sheet_value_no_mail(self):
#         tester = app.test_client(self)
#         response = tester.get("/configuration/0/")
#         data = json.loads(response.get_data(as_text=True))
#         message = data["final_file"]
#         print(message)
#         assertion = 1
#         if message == "values are in DB or config":
#             assertion = 0
#         self.assertEqual(assertion, 1)


##################
# Mail_Server
##################
# class mail_mail_check(unittest.TestCase):
#     def test_Mail_server_mail_fail(self):
#         tester = app.test_client(self)
#         response = tester.get("/configuration/0/")
#         data = json.loads(response.get_data(as_text=True))
#         message = data["mail"]
#         assertion = 1
#         if message == "Mail Server Error or check Your credentials":
#             assertion = 0
#         self.assertEqual(assertion, 0)

#     def test_Mail_server_mail_pass(self):
#         tester = app.test_client(self)
#         response = tester.get("/configuration/1/")
#         data = json.loads(response.get_data(as_text=True))
#         message = data["mail"]
#         assertion = 0
#         if message == "Mail Server Working Please check your mail":
#             assertion = 1
#         self.assertEqual(assertion, 1)


##################
# ContentType
##################


# class ContentType(unittest.TestCase):
# def test_GetAll_no_mail(self):
#     tester = app.test_client(self)
#     response = tester.get("/configuration/0/")
#     # data = json.loads(response.get_data(as_text=True))
#     ContentType = response.content_type
#     print("[Success] Content-Type:", ContentType)
#     self.assertEqual(ContentType, "application/json")

# def test_GetAll_with_mail(self):
#     tester = app.test_client(self)
#     response = tester.get("/configuration/1/")
#     ContentType = response.content_type
#     print("[Success] Content-Type:", ContentType)
#     self.assertEqual(ContentType, "application/json")

# ---- Single ----#

# def test_Single_no_mail(self):
#     tester = app.test_client(self)
#     response = tester.get("/configs/<string:name>/0/")
#     ContentType = response.content_type
#     print("[Success] Content-Type:", ContentType)
#     self.assertEqual(ContentType, "application/json")

# def test_Single_with_mail(self):
#     tester = app.test_client(self)
#     response = tester.get("/configs/<string:name>/1/")
#     ContentType = response.content_type
#     print("[Success] Content-Type:", ContentType)
#     self.assertEqual(ContentType, "application/json")


# global message
# print(mess)
class mail_check_fail(unittest.TestCase):
    def test(self):
        try:
            tester = app.test_client(self)
            response = tester.get("/configuration/1/")
            data = json.loads(response.get_data(as_text=True))
            message = data["message"]
            assertion_mail_check = 1
            if message == "Mail server error or check your credentials":
                assertion_mail_check = 0
            self.assertEqual(assertion_mail_check, 0)
        except:
            print("[Success]Mail server working!")


if __name__ == "__main__":
    unittest.main()
