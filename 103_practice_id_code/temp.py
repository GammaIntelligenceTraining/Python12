import hashlib

password = 'hello'

print(hashlib.md5(password.encode()).hexdigest())
# 5d41402abc4b2a76b9719d911017c592

# if int(idcode[7:10]) in range(1, 11):
#                 bregion = 'Kuressaare haigla'
#             elif int(idcode[7:10]) in range(11, 20):
#                 bregion = 'Tartu Ülikooli Naistekliinik'
#             elif int(idcode[7:10]) in range(21, 151):
#                 bregion = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
#             elif int(idcode[7:10]) in range(151, 161):
#                 bregion = 'Keila haigla'
#             elif int(idcode[7:10]) in range(161, 221):
#                 bregion = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
#             elif int(idcode[7:10]) in range(221, 271):
#                 bregion = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
#             elif int(idcode[7:10]) in range(271, 371):
#                 bregion = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
#             elif int(idcode[7:10]) in range(371, 421):
#                 bregion = 'Narva haigla'
#             elif int(idcode[7:10]) in range(421, 471):
#                 bregion = 'Pärnu haigla'
#             elif int(idcode[7:10]) in range(471, 491):
#                 bregion = 'Haapsalu haigla'
#             elif int(idcode[7:10]) in range(491, 521):
#                 bregion = 'Järvamaa haigla (Paide)'
#             elif int(idcode[7:10]) in range(521, 571):
#                 bregion = 'Rakvere haigla, Tapa haigla'
#             elif int(idcode[7:10]) in range(571, 601):
#                 bregion = 'Valga haigla'
#             elif int(idcode[7:10]) in range(601, 651):
#                 bregion = 'Viljandi haigla'
#             elif int(idcode[7:10]) in range(651, 701):
#                 bregion = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
#             else:
#                 bregion = 'Unknown'