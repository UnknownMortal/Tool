import os
from pyrogram import *
from tool.sos.help import *
from pyrogram.types import *
from folder.basic import edit_or_reply, get_text, get_user


OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", "Join : @M8N_OFFICIAL or @TheInflex")




@Client.on_message(filters.command('clone', ["."]) & filters.me)
async def clone(client: Client, message: Message):
  text = get_text(message)
  tool = await edit_or_reply(message, "Cloning....")
  userk = get_user(message, text)[0]
  user_ = await client.get_users(userk)
  if not user_:
    await tool.edit("Whom i should clone:(")
    return
    
  get_bio = await client.get_chat(user_.id)
  f_name = user_.first_name
  c_bio = get_bio.bio
  pic = user_.photo.big_file_id
  poto = await client.download_media(pic)

  await client.set_profile_photo(photo=poto)
  await client.update_profile(
       first_name=f_name,
       bio=c_bio,
  )
  await message.edit(f"**From now I'm** __{f_name}__")
    

@Client.on_message(filters.command('revert', ["."]) & filters.me)
async def revert(client: Client, message: Message):
 await message.edit("Reverting....")
 r_bio = BIO
	
	#Get ur Name back
 await client.update_profile(
	  first_name=OWNER,
	  bio=r_bio,
	)
	#Delte first photo to get ur identify
 photos = await client.get_profile_photos("me")
 await client.delete_profile_photos(photos[0].file_id)
 await message.edit("**I am back !!**")
 
