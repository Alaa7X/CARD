import requests
print("\033[0;36mBY ALAA7X ")
print("_______________________________________")
print("""
     ___   _           ___       ___   _____  __    __ 
    /   | | |         /   |     /   | |___  | \ \  / / 
   / /| | | |        / /| |    / /| |     / /  \ \/ /  
  / / | | | |       / / | |   / / | |    / /    }  {   
 / /  | | | |___   / /  | |  / /  | |   / /    / /\ \  
/_/   |_| |_____| /_/   |_| /_/   |_|  /_/    /_/  \_\                    
                   
""")
print("=•=•=====•===============•========•====")
card_choose=int(input("1-PLAY STAYOUN\n2-GOOGLE PLAY\n3-ITUNES\n4-XBOX\n5-STC\n~~~~~~~~~~~~~\n>"))
print("=•=•=====•===============•========•====")
if card_choose==1:
	req=requests.get("https://cvcbnhfuu.ml/HMD/api/giftCard.php?type=playstation")
	ply_card=req.json()['Play Station']
	print(f"\ncards:\n{ply_card}")
	print("=======================================")
elif card_choose==2:
	req=requests.get("https://cvcbnhfuu.ml/HMD/api/giftCard.php?type=googleplay")
	google_card=req.json()['Google Card']
	print(f"\ncards:\n{google_card}")
	print("=======================================")
elif card_choose==3:
	req=requests.get("https://cvcbnhfuu.ml/HMD/api/giftCard.php?type=itunes")
	itunes_card=req.json()['itunes Card']
	print(f"\ncards:\n{itunes_card}")
	print("=======================================")
elif card_choose==4:
	req=requests.get("https://cvcbnhfuu.ml/HMD/api/giftCard.php?type=xbox")
	xbox_card=req.json()['Xbox Card']
	print(f"\ncards:\n{xbox_card}")
	print("=======================================")
elif card_choose==5:
	req=requests.get("https://cvcbnhfuu.ml/HMD/api/giftCard.php?type=stc")
	stc_card=req.json()['STC Card']
	print(f"\ncards:\n{stc_card}")
	print("=======================================")
else:
	print("     GOOD 👍")
