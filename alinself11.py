# -*- coding: utf-8 -*-
#Chucky_Bot

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile

alin = LINETCR.LINE() 
alin.login(token="EqHUAEbqMCn7yqJVdK97.X5Bf98jvJqs+mT+eSHtRHW.79KHFGm47S1heS8QSGRz5JUbf4+90N8d2VDGHNCj0/s=")
alin.loginResult()

gr1 = LINETCR.LINE() 
gr1.login(token="EqQpGv5BxNe98v2hRsZ9.LhbHQN1ZFST//xTQDrd+Eq.d173KTXGuA7EXwT9ODlVFyy0DswDHqNruKM80+vbtmM=")
gr1.loginResult()


print "Alin login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""(GHOST RIDER'S)
         GHOST RIDER'S
║Me
║Add
║Cn "text"
║Clockname "text"
║TL:"text"
║Ban:"mid"
║Unban:"mid"
║Bl:on
║Unbl:on
║Mcheck
║Mybio:
║Mybots
║Mymid
║Mygroups
║Message set:"text"
║Message confirm
║Msg add-"text"
║Com set:"text"
║Comment
║Comban/del/cek
║Help set:"text"
║Change
║Gn "text"
║Clink/Curl
║Kick:"mid"
║Invite:"mid"
║Creator
║Contact
║Cancel/Bcancel
║Gcancel:"jumlah"
║Gcancelall
║Ginfo
║Masuk (Masukin bot)
║Bye (Keluarin bot)
║Setlastpoint
║Cctv
║Glink
║Spam on/of "jumlah/text"
║Gurl
║Sc:"mid"
║Blocklist
║Banlist
║Update
║Creator
║Sc "@"
║Fuck "@"
║Sikat "@"
║Spam "@"
║Ban "@" 
║Unban "@"
║Copy "@"
║Nuke
║Backup
║Tag
║Bc "text"
║Say "text"
║Kick@mbl "kick blacklist"
║Ping
║Sett 
║All:
║Allbio:
║All mid
║Respon
║B:out
║B1-2 mid
║B1-2name "text"
║B1-2
║B1-2 gift
║B come
║B1-2 in
║B1-2 bye
═ COMMENT SETTING ═
║Contact:on/off
║Add:on/off
║Join:on/off
║Leave:on/off
║Share:on/off
║Com:on/off
║Clock:on/off
║Pro:on/off
║Prolink:on/off
║Proinvite:on/off
║Procancel:on/off

(GHOST RIDER'S)
"""
helo="====I AM SELF GHOST RIDER'S BOTS"

KAC=[alin,gr1]
mid = alin.getProfile().mid
gr1mid = gr1.getProfile().mid
Bots=[mid,gr1mid]
admsa = "uc796c5f7c2558d04bf32dfc4b214eb87"

wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"""AUTO ADD BY ALIN""",
    "lang":"JP",
    "comment1":"AUTO ADD BY ALIN",
    "comment":"Thanks For Add Me Alin Ghost Rider",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":True,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "copy":True,
    "copy2":"target",
    "target":{}
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


contact = alin.getProfile()
backup = alin.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus


def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = alin.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            alin.rejectGroupInvitation(op.param1)
                        else:
                            alin.acceptGroupInvitation(op.param1)
                    else:
                        alin.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        alin.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace(" ",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    alin.cancelGroupInvitation(op.param1, matched_list)
                    
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
                
        if op.type == 22:
            if wait["leaveRoom"] == True:
                alin.leaveRoom(op.param1)
                
        if op.type == 24:
            if wait["leaveRoom"] == True:
                alin.leaveRoom(op.param1)
                
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "uc796c5f7c2558d04bf32dfc4b214eb87":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            alin.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = alin.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            alin.updateGroup(G)
                        except:
                            alin.sendText(msg.to,"error")
                            
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    alin.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                alin.like(url[25:58], url[66:], likeType=1001)
                gr1.like(url[25:58], url[66:], likeType=1001)
                alin.comment(url[25:58], url[66:], wait["comment1"])
                gr1.comment(url[25:58], url[66:], wait["comment1"])
                
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        alin.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        alin.sendText(msg.to,"Itu tidak berkomentar👈")
                        
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        alin.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        alin.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                        
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        alin.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        alin.sendText(msg.to,"Done👈")
                        
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        alin.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        alin.sendText(msg.to,"Done👈")
                        
                elif wait["contact"] == True:
                    msg.contentType = 0
                    alin.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = alin.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = alin.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        alin.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = alin.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = alin.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        alin.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                        
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    alin.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'help':
                if wait["lang"] == "JP":
                    alin.sendText(msg.to,helpMessage)
                else:
                    alin.sendText(msg.to,helpMessage)
                    
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = alin.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    gr1.updateGroup(group)
                else:
                    alin.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok👈")
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    group = alin.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    alin.updateGroup(group)
                else:
                    alin.sendText(msg.to,"Can not be used for groups other than")
                    
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                alin.kickoutFromGroup(msg.to,[midd])
                
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                alin.findAndAddContactsByMid(midd)
                alin.inviteIntoGroup(msg.to,[midd])
                
            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                alin.sendMessage(msg)
                
            elif "Mybots" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': gr1mid}
                alin.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': gr2mid}
                alin.sendMessage(msg) 
                msg.contentType = 13                
            elif "B1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': gr1mid}
                gr1.sendMessage(msg)
            elif "B2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': gr2mid}
                gr2.sendMessage(msg)
                
            elif "Creator" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ue454f1208a40766f4034d0e7abd6e164'}
                alin.sendMessage(msg)
                
            elif msg.text in ["Bot1 Gift","B1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                gr1.sendMessage(msg)
            elif msg.text in ["Gift","i gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                alin.sendMessage(msg)

            elif msg.text in ["Bot2 Gift","B2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                gr2.sendMessage(msg)

            elif msg.text in ["B Cancel","Cancel dong","Bcancel"]:
                if msg.toType == 2:
                    group = gr1.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        gr1.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            alin.sendText(msg.to,"No invites👈")
                        else:
                            alin.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Tidak ada undangan")
                    else:
                        alin.sendText(msg.to,"invitan tidak ada")

            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = alin.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        alin.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            alin.sendText(msg.to,"No invites👈")
                        else:
                            alin.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        alin.sendText(msg.to,"invitan tidak ada")
            #elif "gurl" == msg.text:
                #print alin.getGroup(msg.to)
                ##alin.sendMessage(msg)
            elif msg.text in ["Clink"]:
                if msg.toType == 2:
                    group = alin.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    alin.updateGroup(group)
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"URL open ô€¨ô€„Œ")
                    else:
                        alin.sendText(msg.to,"URL open ô€¨ô€„Œ")
                else:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        alin.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            elif msg.text in ["Curl"]:
                if msg.toType == 2:
                    group = alin.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    alin.updateGroup(group)
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"URL close ô€¨👈")
                    else:
                        alin.sendText(msg.to,"URL close ô€¨👈")
                else:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        alin.sendText(msg.to,"Can not be used for groups other than ô€œ")
            elif "Ginfo" == msg.text:
              if msg.toType == 2:
#                if msg.from_ in admin:
                  ginfo = alin.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "Error"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventJoinByTicket == True:
                      QR = "Close"
                    else:
                      QR = "Open"
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + "[•]" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Group Status]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                  else:
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
#                else:
                  if wait["lang"] == "JP":
                    alin.sendText(msg.to,"Can not be used outside the group")
                  else:
                    alin.sendText(msg.to,"Not for use less than group")
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                alin.sendMessage(msg)
            elif "Mymid" == msg.text:
                alin.sendText(msg.to,mid)
            elif "B1 mid" == msg.text:
                gr1.sendText(msg.to,gr1mid)
            elif "B2 mid" == msg.text:
                gr2.sendText(msg.to,gr2mid)
            elif "All mid" == msg.text:
                gr1.sendText(msg.to,gr1mid)
                gr2.sendText(msg.to,gr2mid)
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                alin.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+alin.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "All:" in msg.text:
                string = msg.text.replace("All:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = gr1.getProfile()
                    profile.displayName = string
                    gr1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = gr2.getProfile()
                    profile.displayName = string
                    gr2.updateProfile(profile)
                    alin.sendText(msg.to,"􀜁􀇔􏿿semua nama Alin telah di update menjadi\n👉 " + string + "👈")
            elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = gr1.getProfile()
                    profile.statusMessage = string
                    gr1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = gr2.getProfile()
                    profile.statusMessage = string
                    gr2.updateProfile(profile)
            elif "Cn " in msg.text:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = alin.getProfile()
                    profile.displayName = string
                    alin.updateProfile(profile)
                    alin.sendText(msg.to,"􀜁􀇔􏿿Update Names👉 " + string + "👈")
#---------------------------------------------------------
            elif "B1name " in msg.text:
                string = msg.text.replace("B1name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = gr1.getProfile()
                    profile.displayName = string
                    gr1.updateProfile(profile)
                    gr1.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B2name " in msg.text:
                string = msg.text.replace("B2name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = gr2.getProfile()
                    profile.displayName = string
                    gr2.updateProfile(profile)
                    gr2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "â‡‡â‡‡👈")
#--------------------------------------------------------
            elif "Mybio:" in msg.text:
                string = msg.text.replace("Mybio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = alin.getProfile()
                    profile.statusMessage = string
                    alin.updateProfile(profile)
                    alin.sendText(msg.to,"􀜁􀇔􏿿Update Bio👉" + string + "â‡‡â‡‡👈")
#--------------------------------------------------------
            elif "Sc:" in msg.text:
                mmid = msg.text.replace("Sc:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                alin.sendMessage(msg)
            elif msg.text.lower() == 'contact:on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Sudah On")
                    else:
                        alin.sendText(msg.to,"It is already open")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"already open 👈")
                    else:
                        alin.sendText(msg.to,"It is already open 􀜁􀇔􏿿")
            elif msg.text.lower() == 'contact:off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"sudah off ô€œô€„‰👈")
                    else:
                        alin.sendText(msg.to,"It is already off ô€œô€„‰👈")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"off ô€œô€„‰already")
                    else:
                        alin.sendText(msg.to,"already Close ô€œô€„‰👈")
            elif msg.text in ["Pro:on"]:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Protection Enable 􀜁􀇔􏿿👈")
                    else:
                        alin.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Protection Enable􀜁􀇔􏿿")
                    else:
                        alin.sendText(msg.to,"It is already On ô€¨")
            elif msg.text in ['Prolink:on']:
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Link Protection Enable 􀜁􀇔􏿿👈")
                    else:
                        alin.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Link Protect Enable􀜁��􏿿")
                    else:
                        alin.sendText(msg.to,"It is already On ô€¨")
            elif msg.text in ['Proinvite:on']:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Invite Protect Enable 􀜁􀇔􏿿👈")
                    else:
                        alin.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Invite Protect Enable􀜁􀇔􏿿")
                    else:
                        alin.sendText(msg.to,"It is already On ô€¨")
            elif msg.text in ['Procancel:on']:
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Cancel Protection Enable 􀜁􀇔􏿿👈")
                    else:
                        alin.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        alin.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'join:on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        alin.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        alin.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'blocklist':
                blockedlist = alin.getBlockedContactIds()
                alin.sendText(msg.to, "Please wait...")
                kontak = alin.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                alin.sendText(msg.to, msgs)
            elif msg.text.lower() == 'join:off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Auto Join Already Off")
                    else:
                        alin.sendText(msg.to,"Auto Join set off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"already close")
                    else:
                        alin.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Pro:off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Protection Disable ô€œ👈")
                    else:
                        alin.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"already close")
                    else:
                        alin.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Prolink:off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Link Protection Disable ô€œ👈")
                    else:
                        alin.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"already close")
                    else:
                        alin.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Proinvite:off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Invite Protection Disable ô€œ👈")
                    else:
                        alin.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"already close")
                    else:
                        alin.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Procancel:off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Cancel Protection Disable ô€œ👈")
                    else:
                        alin.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"already close")
                    else:
                        alin.sendText(msg.to,"It is already open ô€œ👈")
            elif "Gcancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            alin.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            alin.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            alin.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            alin.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Nilai tidak benar👈")
                    else:
                        alin.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Leave:on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        alin.sendText(msg.to,"Sudah terbuka 􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        alin.sendText(msg.to,"Is already open👈􀜁􀇔􏿿")
            elif msg.text in ["Leave:off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        alin.sendText(msg.to,"Sudah off👈􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        alin.sendText(msg.to,"Is already close👈􀜁􀇔􏿿")
            elif msg.text in ["Share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Done 􀜁􀇔􏿿")
                    else:
                        alin.sendText(msg.to,"Hal ini sudah terbuka👈")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"on👈")
                    else:
                        alin.sendText(msg.to,"on👈")
            elif msg.text in ["Share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        alin.sendText(msg.to,"It is already turned off 􀜁􀇔􏿿👈")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Off👈")
                    else:
                        alin.sendText(msg.to,"Off👈")
            elif msg.text.lower() == 'set':
                md = ""
                if wait["contact"] == True: md+="􀜁􀇔􏿿 Contact:on 􀜁􀄯􏿿\n"
                else: md+="􀜁􀇔􏿿 Contact:off􀜁􀄰􏿿\n"
                if wait["autoJoin"] == True: md+="􀜁􀇔􏿿 Auto Join:on 􀜁􀄯􏿿\n"
                else: md +="􀜁􀇔􏿿 Auto Join:off􀜁􀄰􏿿\n"
                if wait["autoCancel"]["on"] == True:md+="􀜁􀇔􏿿 Auto cancel:" + str(wait["autoCancel"]["members"]) + "􀜁􀄯􏿿\n"
                else: md+= "􀜁􀇔􏿿 Group cancel:off 􀜁􀄰􏿿\n"
                if wait["leaveRoom"] == True: md+="􀜁􀇔􏿿 Auto leave:on 􀜁􀄯􏿿\n"
                else: md+="􀜁􀇔􏿿 Auto leave:off 􀜁􀄰􏿿\n"
                if wait["timeline"] == True: md+="􀜁􀇔􏿿 Share:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Share:off 􀜁􀄰􏿿\n"
                if wait["autoAdd"] == True: md+="􀜁􀇔􏿿 Auto add:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Auto add:off 􀜁��􏿿\n"
                if wait["commentOn"] == True: md+="􀜁􀇔􏿿 Auto komentar:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Auto komentar:off 􀜁􀄰􏿿\n"
                if wait["protect"] == True: md+="􀜁􀇔􏿿 Protect:on 🔓\n"
                else:md+="􀜁􀇔􏿿 Protect:off 🔒\n"
                if wait["linkprotect"] == True: md+="􀜁􀇔􏿿Link Protect:on 🔓\n"
                else:md+="􀜁􀇔􏿿 Link Protect:off🔒\n"
                if wait["inviteprotect"] == True: md+="􀜁􀇔􏿿Invitation Protect:on🔓\n"
                else:md+="􀜁􀇔􏿿 Invitation Protect:off🔒\n"
                if wait["cancelprotect"] == True: md+"􀜁􀇔􏿿 CancelProtect:on 🔓\n"
                else:md+="􀜁􀇔􏿿 Cancel Protect:off 🔒\n"
                alin.sendText(msg.to,md)
                alin.sendText(msg.to,"❂•••••••••✧••••••••••❂")
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ue454f1208a40766f4034d0e7abd6e164'}
                alin.sendMessage(msg)
                alin.sendText(msg.to,"❂•••••{CREATOR GHOST RIDER}•••••❂")
            elif "Gowner" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                alin.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                alin.sendMessage(msg)
            elif cms(msg.text,["Add"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'uc796c5f7c2558d04bf32dfc4b214eb87'}
                alin.sendText(msg.to,"❂•••••••••✧••••••••••❂")
                alin.sendMessage(msg)
                alin.sendText(msg.to,"❂•••••••••✧••••••••••❂")
            elif "Set album:" in msg.text:
                gid = msg.text.replace("Set album:","")
                album = alin.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Tidak ada album👈")
                    else:
                        alin.sendText(msg.to,"Dalam album tidak👈")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "æžš\n"
                        else:
                            mg += str(y["title"]) + ":0 Pieces\n"
                    alin.sendText(msg.to,mg)
            elif "Album" in msg.text:
                gid = msg.text.replace("Album","")
                album = alin.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Tidak ada album")
                    else:
                        alin.sendText(msg.to,"Dalam album tidak")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "\n"
                        else:
                            mg += str(y["title"]) + ":0 pieces\n"
            elif "Hapus album " in msg.text:
                gid = msg.text.replace("Hapus album ","")
                albums = alin.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        alin.deleteAlbum(gid,album["gid"])
                        i += 1
                if wait["lang"] == "JP":
                    alin.sendText(msg.to,str(i) + "Soal album telah dihapus")
                else:
                    alin.sendText(msg.to,str(i) + "Hapus kesulitan album🛡")
            elif msg.text.lower() == 'group id':
                gid = alin.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (alin.getGroup(i).name,i)
                alin.sendText(msg.to,h)
            elif msg.text.lower() == 'b:out':
                gid = gr1.getGroupIdsJoined()
                gid = gr2.getGroupIdsJoined()
                gid = alin.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
                for i in gid:
                    gr1.leaveGroup(i)
                    gr2.leaveGroup(i)
                    alin.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                    ki6.leaveGroup(i)
                if wait["lang"] == "JP":
                    alin.sendText(msg.to,"GHOST RIDER Sudah Keluar Di semua grup")
                else:
                    alin.sendText(msg.to,"He declined all invitations")
            elif msg.text in ["Gcancelall"]:
                gid = alin.getGroupIdsInvited()
                for i in gid:
                    alin.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    alin.sendText(msg.to,"Aku menolak semua undangan")
                else:
                    alin.sendText(msg.to,"He declined all invitations")
            elif "Album deleted:" in msg.text:
                gid = msg.text.replace("Album deleted:","")
                albums = alin.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        alin.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    alin.sendText(msg.to,str(i) + "Soal album telah dihapus👈")
                else:
                    alin.sendText(msg.to,str(i) + "Hapus kesulitan album👈")
            elif msg.text in ["Add:on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Already On")
                    else:
                        alin.sendText(msg.to,"Already On👈")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Already On👈")
                    else:
                        alin.sendText(msg.to,"Already On👈")
            elif msg.text in ["Add:off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Hal ini sudah off👈")
                    else:
                        alin.sendText(msg.to,"Hal ini sudah dimatikan👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Already Off👈")
                    else:
                        alin.sendText(msg.to,"Untuk mengaktifkan-off👈")
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                alin.sendText(msg.to,"We changed the message👈")
            elif "Help set:" in msg.text:
                wait["help"] = msg.text.replace("Help set:","")
                alin.sendText(msg.to,"We changed the Help👈")
            elif "Msg add-" in msg.text:
                wait["message"] = msg.text.replace("Pesan add-","")
                if wait["lang"] == "JP":
                    alin.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    alin.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message confirm"]:
                if wait["lang"] == "JP":
                    alin.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    alin.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    alin.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    alin.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set" in msg.text:
                c = msg.text.replace("Message set","")
                if c in [""," ","\n",None]:
                    alin.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    alin.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Com set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    alin.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    alin.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Comment:on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Aku berada di👈")
                    else:
                        alin.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"ã‚ªãƒ³ã«ã—ã¾ã—ãŸ👈")
                    else:
                        alin.sendText(msg.to,"è¦äº†å¼€👈")
            elif msg.text in ["Com:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Hal ini sudah off")
                    else:
                        alin.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Off👈")
                    else:
                        alin.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                alin.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["Glink","Url"]:
                if msg.toType == 2:
                    g = alin.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        alin.updateGroup(g)
                    gurl = alin.reissueGroupTicket(msg.to)
                    alin.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        alin.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif "gurl+" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl+","")
                    gurl = alin.reissueGroupTicket(gid)
                    alin.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    alin.sendText(msg.to,"ã‚°ãƒ«ãƒ¼ãƒ—ä»¥å¤–ã§ã¯ä½¿ç”¨ã§ãã¾ã›ã‚“👈")
            
            elif "gurl" in msg.text:
                if msg.toType == 1:
                    tid = msg.text.replace("gurl","")
                    turl = gr1.getUserTicket(tid)
                    gr1.sendText(msg.to,"line://ti/p" + turl)
                else:
                    gr1.sendText(msg.to,"error")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = alin.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        alin.updateGroup(x)
                    gurl = alin.reissueGroupTicket(msg.to)
                    alin.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        alin.sendText(msg.to,"Can't be used outside the group")
                    else:
                        alin.sendText(msg.to,"Not for use less than group")
#                else:
#                    alin.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Comban"]:
                wait["wblack"] = True
                alin.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Comban del"]:
                wait["dblack"] = True
                alin.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")
            elif msg.text in ["Comban cek"]:
                if wait["commentBlack"] == {}:
                    alin.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    alin.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +alin.getContact(mi_d).displayName + "\n"
                    alin.sendText(msg.to,mc)
            elif msg.text.lower() == 'Clock:on':
                if wait["clock"] == True:
                    alin.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = alin.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    alin.updateProfile(profile)
                    alin.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'Clock:off':
                if wait["clock"] == False:
                    alin.sendText(msg.to,"Hal ini sudah off🛡")
                else:
                    wait["clock"] = False
                    alin.sendText(msg.to,"Adalah Off")
            elif "Clockname " in msg.text:
                n = msg.text.replace("Jam say ","")
                if len(n.decode("utf-8")) > 30:
                    alin.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    alin.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = alin.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    alin.updateProfile(profile)
                    alin.sendText(msg.to,"Diperbarui👈")
                else:
                    alin.sendText(msg.to,"Silahkan Aktifkan Nama")

            elif "Fuck " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = alin.getGroup(msg.to)
                       ginfo = alin.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       alin.updateGroup(gs)
                       invsend = 0
                       Ticket = alin.reissueGroupTicket(msg.to)
                       alin.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    alin.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    alin.leaveGroup(msg.to)
                                    gs = alin.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    alin.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    alin.updateGroup(gs)
#-----------------------------------------------------------

            elif ("Sikat " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           alin.kickoutFromGroup(msg.to,[target])
                       except:
                           alin.sendText(msg.to,"Error")
            elif ("Ciduk " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           gr1.kickoutFromGroup(msg.to,[target])
                       except:
                           gr1.sendText(msg.to,"Error")
            elif ("Sc " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   key = alin.getContact(key1)
                   alin.sendText(msg.to,"Mid:" +  key1)

            elif "Bro " in msg.text:                  
                       nk0 = msg.text.replace("Beb ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = alin.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    alin.sendText(msg.to,"Good Bye")
#-----------------------------------------------------------
            elif ("Bye " in msg.text):
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      random.choice(KAC).kickoutFromGroup(msg.to,[target])
                   except:
                      pass


            elif ("Ban " in msg.text):
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      alin.sendText(msg.to,"Succes Banned")
                   except:
                      pass

            elif msg.text in ["Mygroups"]:
                 gid = alin.getGroupIdsJoined()
                 h = ""
                 for i in gid:
                  h += "[⭐] %s \n" % (alin.getGroup(i).name + " | Members : " + str(len (alin.getGroup(i).members)))
                 alin.sendText(msg.to, "☆「Group List」☆\n"+ h +"Total Group : " +str(len(gid)))

#----------------------------------------------------------
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = alin.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        alin.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                alin.sendText(msg.to,"Target Unlocked")
                            except:
                                alin.sendText(msg.to,"Error")

            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = alin.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									alin.sendText(msg.to,"Target Locked")
                                except:
                                    alin.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:                  
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = alin.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									alin.sendText(msg.to,"Target Unlocked")
                                except:
                                    alin.sendText(msg.to,"Error")
#-----------------------------------------------------------
            elif msg.text == "Setlastpoint":
                    alin.sendText(msg.to, "Check Yang nyimak")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print wait2

            elif msg.text == "Cctv":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        alin.sendText(msg.to,"======Tercyduck====== %s\n=====Tukang Ngintip======\n%s\nReading point creation date n time:\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                         alin.sendText(msg.to,"An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#-------------------------------------------------
	    elif "Spam @" in msg.text:
#	      if msg.from_ in admin:
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = alin.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
		       alin.sendText(msg.to,"Ghost Rider Squad")
                       alin.sendText(g.mid,"Ghost Rider Squad")
                       gr1.sendText(g.mid,"Ghost Rider Squad")
                       gr2.sendText(g.mid,"Ghost Rider Squad")
                       alin.sendText(g.mid,"Ghost Rider Squad")
                       gr1.sendText(g.mid,"Ghost Rider Squad")
                       gr2.sendText(g.mid,"Ghost Rider Squad")
                       gr1.sendText(g.mid,"Ghost Rider Squad")
                       alin.sendText(msg.to, "Succes")
                       print " Spammed !"
#--------------------------------------------------------------------------
#-----------------------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		alin.sendText(msg.to,"Target Lock")
#-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                text = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (text+"\n")
                if txt[1] == "on":
                    if jmlh <= 1000:
                        for x in range(jmlh):
                            alin.sendText(msg.to, text)
                    else:
                        alin.sendText(msg.to, "Out Of Range!")
                elif txt[1] == "off":
                    if jmlh <= 1000:
                        alin.sendText(msg.to, tulisan)
                    else:
                        alin.sendText(msg.to, "Out Of Range!")

#-----------------------------------------------------------
            elif msg.text.lower() == 'respon':
                profile = gr1.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                gr1.sendText(msg.to, text)
                profile = gr2.getProfile()
                text = profile.displayName + "􀜁􀅔􏿿"
                gr2.sendText(msg.to, text)
#-----------------------------------------------------------speed
            elif msg.text in ["Bl:on"]:
                wait["wblacklist"] = True
                alin.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unbl:on"]:
                wait["dblacklist"] = True
                alin.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == 'mcheck':
                if wait["blacklist"] == {}:
                    alin.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
                else:
                    alin.sendText(msg.to,"􀜁􀇔􏿿 following is a blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "�" +alin.getContact(mi_d).displayName + "\n"
                    alin.sendText(msg.to,mc)
            elif msg.text.lower() == 'banlist':
                if msg.toType == 2:
                    group = alin.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = "❂••••••BLACKLIST••••••❂" + "\n"
                    for mm in matched_list:
                        cocoa += "😂" +alin.getContact(mm).displayName + "\n"
                    alin.sendText(msg.to,cocoa + "❂••••••••••••••••❂")
            elif msg.text.lower() == 'kick@mbl':
                if msg.toType == 2:
                    group = gr1.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        gr1.sendText(msg.to,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            alin.kickoutFromGroup(msg.to,[jj])
                            gr1.kickoutFromGroup(msg.to,[jj])
                            gr2.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass

#---------------------------------------------------
            elif msg.text in ["backup"]:
                    try:
                       alin.updateDisplayPicture(backup.pictureStatus)
                       alin.updateProfile(backup)
                       alin.sendText(msg.to, "Telah kembali semula")
                    except Exception as e:
                       alin.sendText(msg.to, str(e))
#------------------------------------------------
            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    print "[COPY] Ok"
                    _name = msg.text.replace("Copy @","")
                    _nametarget = _name.rstrip(' ')
                    gs = alin.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    sendMessage(msg.to, "Not Found...")
                else:
                     for target in targets:
                         try:
                              alin.cloneContactProfile(target)
                              alin.sendText(msg.to, "success")
                         except Exception as e:
                             print e
#---------------------------------------------- 
#---------------------- = NUKE = ------------------
            elif "Nuke" in msg.text:
                if msg.toType == 2:
                    print "Nuke ok"
                    _name = msg.text.replace("Nuke","")
                    gs = alin.getGroup(msg.to)
                    gs = gr1.getGroup(msg.to)
                    gs = gr2.getGroup(msg.to)
                    start = time.time()
                    gr1.sendText(msg.to, "Nuke Speed")
                    elapsed_time = time.time() - start
                    gr1.sendText(msg.to, "%sseconds" % (elapsed_time))
                    gr2.sendText(msg.to, "Nuke Start")
                    alin.sendText(msg.to, "Nuke Proses")
                    alin.sendText(msg.to,"Ghost Rider Squad")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        alin.sendText(msg.to,"Not found.")
                        ki6.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[cl,ki,ki2]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                alin.sendText(msg,to,"Nuke Finish")
                                gr2.sendText(msg,to,"Nuke Succes Bos")
#-------------------- = NUKE FINISH = ----------------------------- 
#-------------Fungsi Tagall User Start---------------#
            elif msg.text in ["Gr","Tagall","Alka","Tag"]:
                group = alin.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(6)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(7)
                    akh = akh + 1
                    cb2 += "@nrik \n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    alin.sendMessage(msg)
                except Exception as error:
                    print error
#-------------------------------------------------------------
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = alin.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        alin.cancelGroupInvitation(msg.to,[_mid])
                    alin.sendText(msg.to,"I pretended to cancel and canceled👈")
            elif "Album" in msg.text:
                try:
                    albumtags = msg.text.replace("Album","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    alin.createAlbum(gid,name)
                    alin.sendText(msg.to,name + "We created an album👈")
                except:
                    alin.sendText(msg.to,"Error")
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakecâ†’","")
                    alin.sendText(msg.to,str(alin.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        alin.sendText(msg.to,str(e))
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                alin.sendText(msg.to, "Processing Request..")
                elapsed_time = time.time() - start
                alin.sendText(msg.to, "%sseconds" % (elapsed_time))
                gr1.sendText(msg.to, "%sseconds" % (elapsed_time))
                gr2.sendText(msg.to, "%sseconds" % (elapsed_time))
#-----------------------------------------------
            elif msg.text.lower() == 'Masuk':
                        G = alin.getGroup(msg.to)
                        ginfo = alin.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        alin.updateGroup(G)
                        invsend = 0
                        Ticket = alin.reissueGroupTicket(msg.to)
                        gr1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        gr2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = alin.getGroup(msg.to)
                        ginfo = alin.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
                       
#-----------------------------------------------
            elif msg.text.lower() == 'invite':
                        G = alin.getGroup(msg.to)
                        ginfo = alin.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        alin.updateGroup(G)
                        invsend = 0
                        Ticket = alin.reissueGroupTicket(msg.to)
                        gr1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        gr2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = alin.getGroup(msg.to)
                        ginfo = alin.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        gr1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        gr1.updateGroup(G)
            elif msg.text.lower() == 'masuk':
                        G = alin.getGroup(msg.to)
                        ginfo = alin.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        alin.updateGroup(G)
                        invsend = 0
                        Ticket = alin.reissueGroupTicket(msg.to)
                        gr1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        gr2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = alin.getGroup(msg.to)
                        ginfo = alin.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        gr1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        gr1.updateGroup(G)
#-----------------------------------------------
            elif "B1 in" in msg.text:
                        G = alin.getGroup(msg.to)
                        ginfo = alin.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        alin.updateGroup(G)
                        invsend = 0
                        Ticket = alin.reissueGroupTicket(msg.to)
                        gr1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = alin.getGroup(msg.to)
                        ginfo = alin.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        gr1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        gr1.updateGroup(G)
#-----------------------------------------------
            elif "B2 in" in msg.text:
                        G = alin.getGroup(msg.to)
                        ginfo = alin.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        alin.updateGroup(G)
                        invsend = 0
                        Ticket = alin.reissueGroupTicket(msg.to)
                        gr2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = alin.getGroup(msg.to)
                        ginfo = alin.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        gr2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        gr2.updateGroup(G)
#-----------------------------------------------
#-----------------------------------------------
            elif msg.text.lower() == 'Keluar':
                if msg.toType == 2:
                    ginfo = alin.getGroup(msg.to)
                    try:
                        alin.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘")
                        gr1.leaveGroup(msg.to)
                        gr2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B1 Keluar" in msg.text:
                if msg.toType == 2:
                    ginfo = alin.getGroup(msg.to)
                    try:
                        gr1.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B2 Keluar" in msg.text:
                if msg.toType == 2:
                    ginfo = alin.getGroup(msg.to)
                    try:
                        gr2.leaveGroup(msg.to)
                    except:
                        pass
                        
#-----------------------------------------------
            elif "Bye" in msg.text:
                if msg.toType == 2:
                    ginfo = alin.getGroup(msg.to)
                    try:
          #         	alin.leaveGroup(msg.to)
                        gr1.leaveGroup(msg.to)
                        gr2.leaveGroup(msg.to)
####                        alin.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B1 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = alin.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "B2 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = alin.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = alin.getGroup(msg.to)
                alin.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                alin.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
            elif "Bc " in msg.text:
				bctxt = msg.text.replace("Bc ","")
				kisendText(msg.to,(bctxt))
            elif "Say " in msg.text:
				bctxt = msg.text.replace("Say ","")
				gr1.sendText(msg.to,(bctxt))
				gr2.sendText(msg.to,(bctxt))
            elif msg.text.lower() == 'ping':
                gr1.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                gr2.sendText(msg.to,"Ping 􀜁􀇔􏿿")
            
#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in gr1mid:
                        G = gr1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        gr1.updateGroup(G)
                        Ticket = gr1.reissueGroupTicket(op.param1)
                        alin.acceptGroupInvitationByTicket(op.param1,Ticket)
                        gr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        gr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        alin.updateGroup(G)
                    else:
                        G = gr1.getGroup(op.param1)

                            
                        
                        
                        gr1.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        gr1.updateGroup(G)
                        Ticket = gr1.reissueGroupTicket(op.param1)
                        alin.acceptGroupInvitationByTicket(op.param1,Ticket)
                        gr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        gr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        alin.updateGroup(G)
                        gr1.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                       
                        
                elif op.param3 in gr1mid:
                    if op.param2 in gr2mid:
                        G = gr2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        gr2.updateGroup(G)
                        Ticket = gr2.reissueGroupTicket(op.param1)
                        alin.acceptGroupInvitationByTicket(op.param1,Ticket)
                        gr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        gr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        gr2.updateGroup(G)
                    else:
                        G = gr2.getGroup(op.param1)

                        gr2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        gr2.updateGroup(G)
                        Ticket = gr2.reissueGroupTicket(op.param1)
                        alin.acceptGroupInvitationByTicket(op.param1,Ticket)
                        gr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        gr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        gr1.updateGroup(G)


                elif op.param3 in gr2mid:
                    if op.param2 in mid:
                        G = alin.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        alin.updateGroup(G)
                        Ticket = alin.reissueGroupTicket(op.param1)
                        alin.acceptGroupInvitationByTicket(op.param1,Ticket)
                        gr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        gr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        alin.updateGroup(G)
                    else:
                        G = alin.getGroup(op.param1)

                        
                        alin.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        alin.updateGroup(G)
                        Ticket = alin.reissueGroupTicket(op.param1)
                        alin.acceptGroupInvitationByTicket(op.param1,Ticket)
                        gr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        gr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        alin.updateGroup(G)
            except:
                pass
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ks.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    alin.sendText(op.param1,"")
	    else:
		alin.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    alin.sendText(op.param1,"")
	    else:
		alin.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    alin.cancelGroupInvitation(op.param1,[contact.mid for contact in alin.getGroup(op.param1).invitee])
		else:
		    alin.sendText(op.param1,"")
	    else:
		alin.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    alin.cancelGroupInvitation(op.param1,[contact.mid for contact in alin.getGroup(op.param1).invitee])
		else:
		    alin.sendText(op.param1,"")
	    else:
		alin.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = gr1.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    gr1.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    alin.sendText(op.param1,"")
	    else:
		alin.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    alin.sendText(op.param1,str(wait["message"]))
                    gr1.sendText(op.param1,str(wait["message"]))
                    gr2.sendText(op.param1,str(wait["message"]))
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
        if op.type == 55:
            if op.param1 in wait2['readPoint']:
                Name = alin.getContact(op.param2).displayName
                if Name in wait2['readMember'][op.param1]:
                    pass
                else:
                    wait2['readMember'][op.param1] += "\n・" + Name
                    wait2['ROM'][op.param1][op.param2] = "・" + Name
            else:
                alin.sendText

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = alin.getProfile()
                profile.displayName = wait["cName"] + nowT
                alin.updateProfile(profile)
            time.sleep(0.30)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = alin.fetchOps(alin.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(alin.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            alin.Poll.rev = max(alin.Poll.rev, Op.revision)
            bot(Op)


