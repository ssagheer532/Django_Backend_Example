from django.test import TestCase, Client
import json
class SimpleTest(TestCase):
    fixtures = [r"""dummyData.json""", ]
    client = Client()

    def test_getting_existing_program(self):
        response = self.client.get('/modernHealth/programlibrary/get/Program1')
        assert response.status_code == 200
        expected_data = json.loads('''[
    {
        "name": "program1",
        "description": "first program",
        "sections": [
            {
                "name": "firstSection",
                "description": "sample description",
                "overviewImage": "s3://modernHealth/programImages/firstSection.jpg",
                "orderIndex": 1,
                "activityType": "HTML",
                "mcq": [],
                "html": [
                    {
                        "encodedContent": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPG5vdGU+CiAgPHRvPlRvdmU8L3RvPgogIDxmcm9tPkphbmk8L2Zyb20+CiAgPGhlYWRpbmc+UmVtaW5kZXI8L2hlYWRpbmc+CiAgPGJvZHk+RG9uJ3QgZm9yZ2V0IG1lIHRoaXMgd2Vla2VuZCE8L2JvZHk+Cjwvbm90ZT4="
                    },
                    {
                        "encodedContent": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPG5vdGU+CiAgPHRvPlRvdmU8L3RvPgogIDxmcm9tPkphbmk8L2Zyb20+CiAgPGhlYWRpbmc+UmVtaW5kZXI8L2hlYWRpbmc+CiAgPGJvZHk+RG9uJ3QgZm9yZ2V0IG1lIHRoaXMgd2Vla2VuZCE8L2JvZHk+Cjwvbm90ZT4="
                    },
                    {
                        "encodedContent": "PGJvb2tzdG9yZT4gIAogIDxib29rIGNhdGVnb3J5PSJDT09LSU5HIj4gIAogICAgPHRpdGxlIGxhbmc9ImVuIj5FdmVyeWRheSBJdGFsaWFuPC90aXRsZT4gIAogICAgPGF1dGhvcj5HaWFkYSBEZSBMYXVyZW50aWlzPC9hdXRob3I+ICAKICAgIDx5ZWFyPjIwMDU8L3llYXI+ICAKICAgIDxwcmljZT4zMC4wMDwvcHJpY2U+ICAKICA8L2Jvb2s+ICAKICA8Ym9vayBjYXRlZ29yeT0iQ0hJTERSRU4iPiAgCiAgICA8dGl0bGUgbGFuZz0iZW4iPkhhcnJ5IFBvdHRlcjwvdGl0bGU+ICAKICAgIDxhdXRob3I+SiBLLiBSb3dsaW5nPC9hdXRob3I+ICAKICAgIDx5ZWFyPjIwMDU8L3llYXI+ICAKICAgIDxwcmljZT4yOS45OTwvcHJpY2U+ICAKICA8L2Jvb2s+ICAKICA8Ym9vayBjYXRlZ29yeT0iV0VCIj4gIAogICAgPHRpdGxlIGxhbmc9ImVuIj5MZWFybmluZyBYTUw8L3RpdGxlPiAgCiAgICA8YXV0aG9yPkVyaWsgVC4gUmF5PC9hdXRob3I+ICAKICAgIDx5ZWFyPjIwMDM8L3llYXI+ICAKICAgIDxwcmljZT4zOS45NTwvcHJpY2U+ICAKICA8L2Jvb2s+ICAKPC9ib29rc3RvcmU+ICA="
                    }
                ]
            },
            {
                "name": "secondSection",
                "description": "sample description",
                "overviewImage": "s3://modernHealth/programImages/secondSection.jpg",
                "orderIndex": 2,
                "activityType": "MCQ",
                "mcq": [
                    {
                        "question": "first question",
                        "optionOne": "first option",
                        "optionTwo": "second option",
                        "optionThree": "third option",
                        "optionFour": "fourth option",
                        "optionFive": "None"
                    },
                    {
                        "question": "second question",
                        "optionOne": "first option",
                        "optionTwo": "second option",
                        "optionThree": "third option",
                        "optionFour": "fourth option",
                        "optionFive": "None"
                    }
                ],
                "html": [
                    {
                        "encodedContent": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPG5vdGU+CiAgPHRvPlRvdmU8L3RvPgogIDxmcm9tPkphbmk8L2Zyb20+CiAgPGhlYWRpbmc+UmVtaW5kZXI8L2hlYWRpbmc+CiAgPGJvZHk+RG9uJ3QgZm9yZ2V0IG1lIHRoaXMgd2Vla2VuZCE8L2JvZHk+Cjwvbm90ZT4="
                    },
                    {
                        "encodedContent": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPG5vdGU+CiAgPHRvPlRvdmU8L3RvPgogIDxmcm9tPkphbmk8L2Zyb20+CiAgPGhlYWRpbmc+UmVtaW5kZXI8L2hlYWRpbmc+CiAgPGJvZHk+RG9uJ3QgZm9yZ2V0IG1lIHRoaXMgd2Vla2VuZCE8L2JvZHk+Cjwvbm90ZT4="
                    },
                    {
                        "encodedContent": "PGJvb2tzdG9yZT4gIAogIDxib29rIGNhdGVnb3J5PSJDT09LSU5HIj4gIAogICAgPHRpdGxlIGxhbmc9ImVuIj5FdmVyeWRheSBJdGFsaWFuPC90aXRsZT4gIAogICAgPGF1dGhvcj5HaWFkYSBEZSBMYXVyZW50aWlzPC9hdXRob3I+ICAKICAgIDx5ZWFyPjIwMDU8L3llYXI+ICAKICAgIDxwcmljZT4zMC4wMDwvcHJpY2U+ICAKICA8L2Jvb2s+ICAKICA8Ym9vayBjYXRlZ29yeT0iQ0hJTERSRU4iPiAgCiAgICA8dGl0bGUgbGFuZz0iZW4iPkhhcnJ5IFBvdHRlcjwvdGl0bGU+ICAKICAgIDxhdXRob3I+SiBLLiBSb3dsaW5nPC9hdXRob3I+ICAKICAgIDx5ZWFyPjIwMDU8L3llYXI+ICAKICAgIDxwcmljZT4yOS45OTwvcHJpY2U+ICAKICA8L2Jvb2s+ICAKICA8Ym9vayBjYXRlZ29yeT0iV0VCIj4gIAogICAgPHRpdGxlIGxhbmc9ImVuIj5MZWFybmluZyBYTUw8L3RpdGxlPiAgCiAgICA8YXV0aG9yPkVyaWsgVC4gUmF5PC9hdXRob3I+ICAKICAgIDx5ZWFyPjIwMDM8L3llYXI+ICAKICAgIDxwcmljZT4zOS45NTwvcHJpY2U+ICAKICA8L2Jvb2s+ICAKPC9ib29rc3RvcmU+ICA="
                    }
                ]
            }
        ]
    }
]''')
        assert str(response.content) == 'b\'' + str(json.dumps(expected_data)) + '\''

    def test_getting_nonexistent_program(self):
        response = self.client.get('/modernHealth/programlibrary/get/randomProgram')
        assert response.status_code == 400
        assert str(response.content) == 'b\'{"Status": "Program name does not exist"}\''

    def test_using_post_request(self):
        response = self.client.post('/modernHealth/programlibrary/get/program1')
        assert response.status_code == 405
        assert str(response.content) == 'b\'{"Status": "405 Method Not Allowed"}\''
