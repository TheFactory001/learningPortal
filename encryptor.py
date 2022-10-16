from cryptography.fernet import Fernet
 
# we will be encrypting the below string.
message = {
  "type": "service_account",
  "project_id": "thefactory",
  "private_key_id": "4f1eb8f607f9293deccbff44dc40ca46b5e055a5",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDjUSO3uL/5vASt\nYNR0hDOCreV+6+Z372b3BZTRYgmuEDJOMqmhsFc+6Ph1u+UqPxDqfhd57sjMDA7y\nSsnQudtvsZE5GwQXiuGc4Lbq2ncAmHpgeBfgthA72/7adaEI4OMBveEKgbLRt2Pi\n61ZybefysLrr/j6oifM13Iw0o7aEkiP+K8xsvUoRa7S3rfwSedKApGY9GeEVNHjP\nEjOhq0lYKKO3SOn/ZvkVoLzybhiLAX2TTlC/pY6z93ZIzyf3THgqVfaD872Nr5EL\nwabBbZWSPvhlvyQCCIyCTWdK7SS5tZsn5ECWj6isdiDZDRjzksu9p34cB1Py/+QU\nwo2rPxHHAgMBAAECggEANt7Ro9ntQS+Q43cBoaR9uJgYUxRHXAEGVi9bNlWXZ5RS\nSEzzZGuoC6/5tZWm4hU6FJheO1kX0CVDAFpsL72FSgdPOj0atkIYZqFZlgQpAJRN\nyfaDMQNRlNlsQbhuKDH8qeF3Lm2TSAsgCdjr05BTEmJ1pFyJLG6sLf6wO06fUo1t\nuiUpmFjJNjvroLO7yfvYTjDD3VfTpduJXAzjQFMuu0tryQujWvaAB+vJhXibHdnv\nDfhNP4jsSyWb+xD1N5uEto/jlw1eVbxgKkj0nypFi4AeYCgrq51JwFSFhZ/GMoEw\nmW+JQyAWcrHpFiZtL4o8DIWIyYTXhywmd3q0sBRZgQKBgQDz1HJ+1rx0PfuRmgNN\n98pSgfBneZ7yRLWdJ5ghzvwcso50b9vQWJfQI1gCc6PMPlN3/7CSB+asDiyEWMwt\nyrrf2Eg8SGK2M9pJ5x2PlTfYIMXWaj8OW3W/JGHcZT3ySbd9UysmWnE0mc1/hp/M\nuwRRV5coAZ8rStsUZEqMNsVRRwKBgQDuqbKCtpCC240rwWE8VltIALFCabyaEkyG\n2RzitDrSJXM7YlS29euFHY8n6uVQO4qoBMqPHpEdocXgu46OKZyR1o4FNRotf+Yw\ntiT+hEC7j8nemhSgiGr8uSUVAUEw3P36L9Qj7PK+Pbb2noiHDZv9Nt/Gi/tpSBjw\nap0soBx7gQKBgE8JwsOS4CveG7oq7n9Ln233aPJh3kAyPZzfxNTQv7CdwMfFqr9y\nuGNj0ZeZ3LLMUUpIu/faT8/eGFgeYLFHUiRVe7Tu0fC2BkCGhnKQsDWDCh5i+mWx\nCA4ZwQ8sUlRDyRL67rXUA3ZFlPONtCctSE0F053ISMxDy5hkmjWxW2zpAoGAJGQZ\nxRajWGCz2O0mr3WXe5YncTIAQRnzM0idv++tXGe7d12Z/z/mRqjoMDT//Ejn7pC0\ndjg59mO5cXgH16N+rToi86ZSNIfhCKJtZ6Ww3Siipl+mL4g9kAWHIvnK//FihKiQ\nV14E8X8li9tGhBlOJMEeQ/8KOdZ1fwsypiBP14ECgYAIEYadyYk5zhop2BK5mr+D\nNnVFJdd4qSpR/OFsRkwoqE9OumxfbSXeUhf0yFleCDM8Quc6tP/9pgmpREzDUlEK\nODufoU/lKxjF0tR8zc2xM43N8Ik6fHVyJIcycGqgsl8qbbLYv5Udh5LtOTf8yFS+\ndKPYB8TLNDC8xOP4gxjMPw==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-xxfjn@thefactory.iam.gserviceaccount.com",
  "client_id": "116491680580709943723",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-xxfjn%40thefactory.iam.gserviceaccount.com"
}

chnsg = str(message)

print(chnsg)
 
# generate a key for encryption and decryption
# You can use fernet to generate
# the key or use random key generator
# here I'm using fernet to generate key
 
key = Fernet.generate_key()
print("key ", key.decode("utf-8"))
 
# Instance the Fernet class with the key
 
fernet = Fernet(key)
 
# then use the Fernet class instance
# to encrypt the string string must
# be encoded to byte string before encryption
encMessage = fernet.encrypt(chnsg.encode())
 
print("original string: ", chnsg)
print("encrypted string: ", encMessage)
 
# decrypt the encrypted string with the
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods
decMessage = fernet.decrypt(encMessage).decode()
 
print("decrypted string: ", decMessage)