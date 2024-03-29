o
    �T�bW  �                   @   s
  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlZd dlZd dlZd dlmZmZmZ d dlmZ d dlmZmZmZmZmZmZmZ d dlmZ d dlm Z  d dlm!Z! d dl"m#Z# d d	lm$Z$m%Z%m#Z#m&Z&m'Z'm(Z(m)Z) d d
l*m+Z+m,Z,m-Z- d dl.m/Z/ d dl0m1Z1m2Z2m3Z3m4Z4m5Z5m6Z6m7Z7m8Z8m9Z9m5Z5m9Z9m7Z7m:Z: d dl;m<Z< d dlm=Z=m>Z> d dl?m@Z@ d dlZd dlAmAZAmBZBmCZC d dlZe�D� ZEeE�Fd� eEd d ZGeEd d ZHeEd d ZIeEd d ZJejK�Ld��se�Md� ejK�Ld��s#e�Md� e�Md� eNdd� ejK�Ld��s/eNdd� eOeG�ZPeQeH�ZReQeJ�ZSeQeI�ZTej=dePeReSd�ZUeNddd ��6ZVej!eVd!d"d#�ZWeXeWd� g ZYeWD ]ZZeA�[� eA�\eZd$ � d%� Z]eA�\d&d%�eA�\d'd%� Z^�q`W d  � n	1 �s�w   Y  eU�_e>j`e>�ad(g�@ �d)d(� �ZbeU�_e>j`e>�ad*g�@ �d+d*� �ZceU�_e>j`e>�ad,g�@ �d-d,� �ZdeU�_e>j`e>�ad.g�@ �d/d0� �ZeeU�_e>j`e>�ad1g�@ �d2d(� �ZbeU�_e>j`e>�ad3g�@ �d4d(� �ZbeU�f� d5d6� �Zgd7Zheieh� eid8� eU�j�  dS )9�    N)�InlineKeyboardButton�InlineKeyboardMarkup�Message)�TimeoutError)�SessionPasswordNeeded�	FloodWait�PhoneNumberInvalid�ApiIdInvalid�PhoneCodeInvalid�PhoneCodeExpired�UserNotParticipant)r   )�ChatMethods)�reader)�TelegramClient)�	functions�typesr   �
connection�sync�utils�errors)�GetFullChannelRequest�JoinChannelRequest�InviteToChannelRequest)�SessionPasswordNeededError)�PhoneCodeExpiredError�PhoneCodeInvalidError�PhoneNumberBannedError�PhoneNumberInvalidError�UserBannedInChannelError�PeerFloodError�UserPrivacyRestrictedError�ChatWriteForbiddenError�UserAlreadyParticipantErrorr   r"   r    �ChatAdminRequiredError)�StringSession)�Client�filters)�listen)�datetime�	timedelta�datez
config.iniZTelegram�export_api_id�export_api_hash�export_updates_channel�export_bot_tokenz
./sessions�Users/5166763124/phone.csvz./Usersz./Users/5166763124�w�data.csv�app)Zapi_idZapi_hashZ	bot_token�UTF-8��encoding�,�
�Z	delimiter�lineterminator�   �%Y-%m-%d�
2021-12-01�
2021-11-03�startc                 �   s�   �t j�d|jj� d��s"t �d|jj� �� td|jj� d�d� |jj}|jjr0d|jj nd }tt	ddd�t	d	d
d�gt	ddd�t	ddd�gt	ddd�gg�}|j
d|jj� d�|d�I d H  d S )N�Users/�
/phone.csv�./Users/r0   �@u   Login✅�Login)Zcallback_datau
   Adding💯�Addingu   Phone⚙️�Editu   PhoneSee💕�Ishu   Phone Remove⚙️�Removez**Hi** `u�   ` **!

I'm Induced Scraper Bot 
Made for doing Scraping for free,
Without Using Any Use of Python.
Credit - Ishan, GodMrunal, HellDshot
Made with ❤️ By @pornhubadder**)Zreply_markup)�os�path�exists�	from_user�id�mkdir�open�usernamer   r   Z
reply_text�
first_name)�lel�messagerL   Z	user_nameZbut� rS   �/storage/emulated/0/mtg/main.pyr>   4   s   �@$�phonec              
   �   sl  ��z�t j�d|jj� d��s$t �d|jj� �� td|jj� d�d� td|jj� d�d���W}dd� t�|�D �}g }d}|D ]}|d	7 }|�	t
|�� qAtj|jjd
d�I d H }t|j�}||7 }|d	k r}t�|jjd�I d H  	 W d   � W d S |dkr�t�|jjdd| � d��I d H  	 W d   � W d S td	|d	 �D ]Z}	tj|jjdd�I d H }|j}
d|
v r�t�|jjd�I d H  q�t|
�dks�t|
�dks�t|
�dkr�t
|
�}|�	|� t�|jjd|� d|
� d��I d H  q�t�|jjd�I d H  q�tt�|��}td|jj� d�ddd��}tj|dd�}|�|� W d   � n	1 �s*w   Y  td|jj� d���3}td|jj� d�d��}|D ]}|�|�dd �� �qHW d   � n	1 �s`w   Y  W d   � n1 �spw   Y  W d   � W d S W d   � W d S 1 �s�w   Y  W d S  t�y� } zt�|jjd!|� d"��I d H  W Y d }~d S d }~ww )#Nr?   r@   rA   r0   �rc                 S   �   g | ]}|d  �qS �r   rS   ��.0�rowrS   rS   rT   �
<listcomp>J   �    zphone.<locals>.<listcomp>r   �   uU   **Enter number of accounts to Login (in intiger)

Made with ❤️ By @pornhubadder**��chat_id�textuK   **Invalid Format less then 1 Try again

Made with ❤️ By @pornhubadder**�d   z**You can add only u/    Phone no 

Made with ❤️ By @pornhubadder**u�   **Now Send Your Telegram Account's Phone Number in International Format. 
Including **Country Code**. 
Example: **+14154566376 = 14154566376 only not +**

Made with ❤️ By @pornhubadder**�+uB   **As Mention + is not include

Made with ❤️ By @pornhubadder**�   �   �   �**z
). Phone: u8    Set Sucessfully✅

Made with ❤️ By @pornhubadder**uF   **Invalid Number Format Try again

Made with ❤️ By @pornhubadder**�/1.csvr3   r4   r7   �r9   r6   � �	**Error: �%   

Made with ❤️ By @pornhubadder**)rH   rI   rJ   rK   rL   rM   rN   �csvr   �append�strr2   �ask�chat�intra   �send_message�range�len�list�dict�fromkeys�writer�	writerows�write�replace�	Exception)rQ   rR   �f�str_list�
NonLimited�a�pphone�number�n�irU   �Singla�	writeFilery   �infile�outfile�line�erS   rS   rT   rU   B   sj   �
�"�$
&�.���  �(�"���loginc                 �   s�  ��z�t d|jj� d�d����}g }g }dd� t�|�D �}d}d}|D �]�}�z�tt�|��}	td|	� �t	t
�}
|
�� I d H  |
�� I d H �s�z
|
�|	�I d H  W nW ty{ } z|�d|j� d	��I d H  W Y d }~W  W d   � W d S d }~w ty�   |�d
�I d H  Y W  W d   � W d S  ty�   |�|	� d��I d H  Y W q$w ztj|jjddd�I d H }W n ty�   |�d�I d H  Y W  W d   � W d S w |j}z|
j|	d�t|��d�I d H  W n� t�y   |�d�I d H  Y W  W d   � W d S  t�y    |�d�I d H  Y W  W d   � W d S  t�y�   ztj|jjddd�I d H }W n t�yS   |�d�I d H  Y Y W  W d   � W d S w z|
j|jd�I d H  W nZ t�y� } z|�dt|�� d��I d H  W Y d }~Y W  W d   � W d S d }~w t�y� } z"t�|jjdt|�� d��I d H  W Y d }~Y W  W d   � W d S d }~ww Y nw t dd���}dd� t�|�D �}g }|D ]
}|� t|�� �q�t|	�}|� |� t!t"�#|��}t dddd��}tj$|dd �}|�%|� W d   � n	1 �sw   Y  t d��-}t dd��}|D ]}|�&|�'d!d"�� �qW d   � n	1 �s6w   Y  W d   � n	1 �sFw   Y  W d   � n	1 �sVw   Y  t(�)d� |
t*j+j,d#d$��I d H  |
�d%d&�I d H  t|
�-d%�I d H �}d'}||v �r�d(}|d)7 }|� t|	�� n	d*}|� t|	�� |
�.� I d H }t�|jjd+|j/� d,|j0� d-|	� d.|� d/�	�I d H  |d)7 }|
�1� I d H  W q$ t2�y�   |
�1� I d H  |
�� I d H  Y q$ t3�y�   t�|jjd0�I d H  Y q$ t�y } zt�|jjd1|� d2��I d H  W Y d }~q$d }~ww |D ]
}|� t|�� �qt d|jj� d3�ddd��}tj$|dd �}|�%|� W d   � n	1 �sJw   Y  t d|jj� d3���3}t d|jj� d�d��}|D ]}|�&|�'d!d"�� �qhW d   � n	1 �s�w   Y  W d   � n	1 �s�w   Y  t�|jjd4|� d5|� d6��I d H  W d   � W d S 1 �s�w   Y  W d S  t�y� } zt�|jjd1|� d2��I d H  W Y d }~d S d }~ww )7Nr?   r@   rV   c                 S   rW   rX   rS   rY   rS   rS   rT   r\   y   r]   zlogin.<locals>.<listcomp>r   �	sessions/zYou Have Floodwait of z Secondsz;Your Phone Number is Invalid.

Press /start to Start Again!z	 is Banedz�An OTP is sent to your phone number, 
Please enter OTP in `1 2 3 4 5` format. __(Space between each numbers!)__ 

If Bot not sending OTP then try /restart and Start Task again with /start command to Bot.
Press /cancel to Cancel.i,  )Ztimeoutz9Time Limit Reached of 5 Min.
Press /start to Start Again!� )rU   �codez+Invalid Code.

Press /start to Start Again!z.Code is Expired.

Press /start to Start Again!zDYour Account Have Two-Step Verification.
Please Enter Your Password.z<`Time Limit Reached of 5 Min.

Press /start to Start Again!`)�passwordz**ERROR:** `�`r/   c                 S   rW   rX   rS   rY   rS   rS   rT   r\   �   r]   z1.csvr0   r3   r4   r7   ri   r6   rj   z@SpamBot)rL   ZSpamBotz/startZbirduT   Good news, no limits are currently applied to your account. You’re free as a bird!r^   zyou are limitedu'   Login Successfully✅ Done.

**Name:** z
**Username:** z
**Phone:** z
**SpamBot Stats:** �'   

**Made with ❤️ By @pornhubadder**uv   **You have not enter the phone number 
please edit Config⚙️ by camand /start.

Made with ❤️ By @pornhubadder**rk   rl   rh   z**All Acc Login z Account Available of u&    

Made with ❤️ By @pornhubadder**)4rN   rK   rL   rm   r   rr   r   �parse_phoner   �APP_ID�API_HASH�connectZis_user_authorizedZsend_code_requestr   Zreply�xr   r   r2   rp   rq   r   ra   Zsign_in�joinro   r   r   r   r}   rs   rn   rv   rw   rx   ry   rz   r{   r|   rH   �remover   ZcontactsZUnblockRequestZget_messagesZget_merP   rO   �
disconnect�ConnectionError�	TypeError)rQ   rR   r~   rV   �lr   Zpo�sr�   rU   �clientr�   ZotpZotpsZtwo_step_coder�   r�   r�   ry   r�   r�   r�   �msg�reZstats�meZishrS   rS   rT   r�   r   s  �
�����"�"�%�(��0"��0��
���� ��

4*���.��� &(�a��Zaddingc                 �   s  ��zgt j|jjdd�I d H }|j}t j|jjdd�I d H }|j}t j|jjdd�I d H }t|j�}|}�ztd|jj� d�d����}dd	� t�	|�D �}|D �]�}	d
}
d
}d
}d}t
�|	�}td|� �tt�}|�� I d H  |t|��I d H  t j|jjdd�I d H  |j|dd�2 �z�3 d H W }zd|d7 }||k r�W q�|| dkr�|�� I d H  |d7 }t j|jj|� d�I d H  t �|jjd|� d��I d H  W  �n^|dkr�|d7 }t j|jj|� d�I d H  d}d
}|t||g��I d H  d}W �n tj�y; } z7d|j� d�}|�� I d H  |d7 }t j|jj|� d�I d H  t j|jjd|j� d�d�I d H  W Y d }~ n�d }~w t�yF   d}Y n� t�yQ   d}Y n� t�y\   d}Y n� t�yg   d}Y n� t�y�   d}|�� I d H  t j|jj|� d�I d H  Y  n� t�y�   |
d k�r�|�� I d H  t j|jj|� d�I d H  t j|jjd!d�I d H  Y  nvd"}|
d7 }
Y nR t�y� } z|t|��I d H  W Y d }~q�d }~w tj�y� } z
|j j!}W Y d }~n$d }~w t"�y } z|}W Y d }~nd }~w   t#�$�  d#}Y  n||| d � d$|j%� d%|� d&�7 }|d7 }|d7 }q�6 qOW d   � n1 �s8w   Y  W W d S W W d S  t"�yi } zt j|jjd'|� d(�d�I d H  W Y d }~W d S d }~ww  t"�y� } zt �|jjd|� d)��I d H  W Y d }~d S d }~ww )*NuH   **Now Send the From Group Username 

Made with ❤️ By @pornhubadder**r_   uF   **Now Send the To Group Username 

Made with ❤️ By @pornhubadder**u<   **Now Send Start From  

Made with ❤️ By @pornhubadder**r?   r@   rV   c                 S   rW   rX   rS   rY   rS   rS   rT   r\   �   r]   zto.<locals>.<listcomp>r   z**Adding Start**

r�   z**Scraping Start**i|  )�limitr^   �   �&   **
Made with ❤️ By @pornhubadder**rk   uI    Due to Some Error Moving to Next no

Made with ❤️ By @pornhubadder**�(   ZDONEzFloodWaitError for z secz**FloodWaitError for z sec
Moving To Next Number**ZPrivacyRestrictedErrorZALREADYzUser BannedzTo Add Admin RequiredzError In Entry�
   z1**Too Many PeerFloodError
Moving To Next Number**r   zUnexpected Errorz). **u   **   ⟾   **z**
zError: u%    

 Made with ❤️ By @pornhubadderrl   )&r2   rp   rq   rL   ra   rr   rN   rK   rm   r   r   r�   r   r�   r�   r�   r   rs   Ziter_participantsr�   r   r   ZFloodWaitErrorZsecondsr    r"   r   r#   �
ValueErrorr   r!   ZRPCError�	__class__�__name__r}   �	traceback�	print_excrP   )rQ   rR   r�   ZFromZTor�   Zdir~   r   r�   ZpeerZra�dadrV   rU   r�   r�   �statusr�   Zcwfe�dr�   rS   rS   rT   �to�   s�   �



"�
���$
���.�H0����r�   Zphoneseec           	   
   �   s  �ztt d|jj� d�d��^}dd� t�|�D �}d}d}d}|D ]0}|d7 }|d7 }|d	krC|d
7 }tj|jj|� d�I d H  d}d}|d|� dt|�� d�7 }q |d
7 }tj|jj|� d�I d H  W d   � W d S 1 snw   Y  W d S  t	y� } zW Y d }~d S d }~ww )Nr?   r@   rV   c                 S   rW   rX   rS   rY   rS   rS   rT   r\   @  r]   �start.<locals>.<listcomp>z**Your Phone Numbers are**

r   r^   r�   r�   r_   rg   z).** `z`
)
rN   rK   rL   rm   r   r2   rs   rq   rr   r}   )	rQ   rR   r~   r   �de�dar�   r�   r�   rS   rS   rT   r>   ;  s.   �&���r�   c              
   �   s�  �z�z�t d|jj� d�d���}dd� t�|�D �}|j tj|jjdd�I d H }t	|� |�
|j� t d|jj� d�d	d
d��}tj|dd�}|�|� W d   � n1 sVw   Y  t d|jj� d���1}t d|jj� d�d	��}|D ]}	|�|	�dd�� qtW d   � n1 s�w   Y  W d   � n1 s�w   Y  tj|jjdd�I d H  W d   � n1 s�w   Y  W W d S W W d S  ty� }
 zW Y d }
~
W d S d }
~
ww  ty� } zt�|jjd|� d��I d H  W Y d }~d S d }~ww )Nr?   r@   rV   c                 S   rW   rX   rS   rY   rS   rS   rT   r\   [  r]   r�   u<   **Send Number to remove

Made with ❤️ By @pornhubadder**r_   rh   r0   r3   r4   r7   ri   r6   rj   �Done SucessFullyrk   rl   )rN   rK   rL   rm   r   �closedr2   rp   rq   �printr�   ra   ry   rz   r{   r|   rs   r}   )rQ   rR   r~   r   r�   r�   ry   r�   r�   r�   r�   r�   rS   rS   rT   r>   U  s>   ��.��� ,�����c                 �   s  �|j }d|v r|j�� I d H  | �|jjjd�I d H  d S d|v r8|j�� I d H  | �|jjjd�I d H  d S d|v rR|j�� I d H  | �|jjjd�I d H  d S d|v rl|j�� I d H  | �|jjjd�I d H  d S d	|v r�|j�� I d H  | �|jjjd
�I d H  d S d|v r�|j�� I d H  | �|jjjd�I d H  d S d|v r�|j�� I d H  | �|jjjd�I d H }t| �I d H }|�d|d � d|d � ��I d H  d S d|v �ra|j�� I d H  | j|jjjdd�I d H }t	|j
�}tddd��^}tj|ddd�}t|d � |j tdddd�}tj|ddd�}	|	�g d�� d}
|D ]}|	�|
|d |d g� |
d7 }
�q#|	�|
|t�� g� | j|jjjdd�I d H  W d   � d S 1 �sZw   Y  d S d |v �r�|j�� I d H  tddd��d}tj|ddd�}t|d � d!}d}
|D ]6}t�� t�|d � d"� }t�d#d"�t�d$d"� }||k�r�|
d7 }
||
� d%|d � d&|d � d�7 }�q�|d'7 }| j|jjj|d�I d H  W d   � d S 1 �s�w   Y  d S d(|v �r�z�t� I d H }d}
d}| j|jjjd)d�I d H }|j
}|D ]M}t	|d �}z| jt	|�|� d*d+d,�I d H  |
d7 }
W �q t�yD } zt�|j�I d H  |d7 }W Y d }~�qd }~w t�yR   |d7 }Y �qw | �|jjjd-|
� d.|� d/��I d H  W d S  t�y� } z| �|jjjd0|� d1��I d H  W Y d }~d S d }~ww d S )2NrC   u|   **There is nothing no more..!
Just Click on /login to login and check stats of Account.

Made with ❤️ By @pornhubadder**rF   u   **There is nothing no more..!
Just Click on /phonesee to login and check stats of Account.

Made with ❤️ By @pornhubadder**rG   u}   **There is nothing no more..!
Just Click on /remove to login and check stats of Account.

Made with ❤️ By @pornhubadder**rD   u   **There is nothing no more..!
Just Click on /adding to start adding from Login✅ Account.

Made with ❤️ By @pornhubadder**rE   u|   **There is nothing no more..!
Just Click on /phone to login and check stats of Account.

Made with ❤️ By @pornhubadder**ZHomeuc   **There is nothing no more..!
Just Click on /start to Go Home.

Made with ❤️ By @pornhubadder**ZUserszPlease Wait...zTotal:

Users - r   z
Blocked - r^   ZNewu?   **Send User Id Of New User

Made with ❤️ By @pornhubadder**r_   r1   r3   r4   r6   r7   r8   r0   )zsr. no.zuser idZDater:   r�   ZCheckz**Premium Users**
r;   r<   r=   z). z - r�   Z	BroadcastuC   **Now me message For Broadcast

Made with ❤️ By @pornhubadder**ZmarkdownT)r`   ra   Z
parse_modeZdisable_web_page_previewzSuccessfully Broadcasted to z Chats
Failed - z Chats !rk   rl   )�datarR   �deleters   rq   rL   Z
users_infoZeditrp   rr   ra   rN   rm   r   �nextr�   ry   Zwriterowr*   �todayr(   �strptimeZ	query_msgr   �asyncio�sleepr�   r}   )r2   �update�kr�   �messagesr�   rU   r~   �rowsry   r�   r�   �Er[   r�   rV   �query�br`   r�   rS   rS   rT   �buttonn  s�   �(


$�


"�$�
��,.���r�   zV
------------------------------
         @pornhubadder
------------------------------
z*Pornhub Adding Started Sucessfully........)kr�   rH   Zrandomr�   ZhtmlZconfigparserZpyrogram�
subprocessZrequests�timer�   ZloggingZtelethonrm   Zjson�sysZpyrogram.typesr   r   r   Zasyncio.exceptionsr   Zpyrogram.errorsr   r   r   r	   r
   r   r   Z*pyrogram.errors.exceptions.bad_request_400Ztelethon.client.chatsr   r   Ztelethon.syncr   r   r   r   r   r   r   Ztelethon.tl.functions.channelsr   r   r   Ztelethon.errorsr   Ztelethon.errors.rpcerrorlistr   r   r   r   r   r   r    r!   r"   r#   Ztelethon.sessionsr$   r%   r&   Zpyromodr'   r(   r)   r*   ZConfigParserZconfig�readr+   r,   r-   r.   rI   rJ   rM   rN   rr   r�   ro   r�   Z	BOT_TOKENZUPDATES_CHANNELr2   r~   r�   r�   Zishanr[   r�   r�   r�   rV   Z
on_messageZprivateZcommandr>   rU   r�   r�   Zon_callback_queryr�   ra   r�   �runrS   rS   rS   rT   �<module>   s�   � $$<






��


/
k
\


T