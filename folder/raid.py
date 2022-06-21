from folder.file import dbb

Rbun = dbb["RBAN"]


async def rtool(user, reason="#MATHERCHOD"):
    await Rbun.insert_one({"user": user, "reason": reason})


async def runtool(user):
    await Rbun.delete_one({"user": user})


async def rban_list():
    return [lo async for lo in Rbun.find({})]


async def toolub_info(user):
    kk = await Rbun.find_one({"user": user})
    if not kk:
        return False
    else:
        return kk["reason"]
