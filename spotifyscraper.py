#!/usr/bin/env python
import urllib, json
import scraperwiki

#Set up the token - this only lasts for an hour after which you will need to generate a new one
token = 'BQA5m6oNalpO2oVIZ1ogAklMWzj_Kkk3oJBCn8fasnADDacSi7JmME830Cx3NCl5I7lSGClpBSUwkG3NblvPDw'

baseurl = 'https://api.spotify.com/v1/artists/'
#These artist IDs have been compiled through a combination of scraping and manual search
artists = ['711MCceyCBcFnzjGY4Q7Un','3QP0XPDwbvGivqDAaJ5f5G','4dpARuHxo51G3z768sgnrY','7Ey4PD4MYsKc5I2dolUwbH','3XHO7cRUPCLOr6jwp8vsx5','3FTxQTEzrX6tcJYSlsdUle','4kwxTgCKMipBKhSnEstNKj','4fxp616ALtFWnXfwxnjLzW','3kjuyTCjPG1WMFCiyc5IuB','7Ln80lUS6He07XvHI8qqHH','2evydP72Z45DouM4uMGsIE','2ziB7fzrXBoh1HUPS6sVFn','0nmQIMXWTXfhgOBdNzhGOs','1vCWHaC5f2uS3yhpwWbIA6','7gRhy3MIPHQo5CXYfWaw9I','244fcyNSuyhbRlMGfMbYrO','4YrKBkKSVeqDamzBPWVnSJ','7EQ0qTo7fWT7DPxmxtSYEc','6l77PmL5iuEEcYjGl8K6s7','56ZTgzPBDge0OvCGgMO3OY','03r4iKL2g2442PT9n2UKsx','6pmxr66tMAePxzOLfjGNcX','4I2BJf80C0skQpp1sQmA0h','79fyBJJSUvWw4263rXYDM0','5schNIzWdI9gJ1QRK8SBnc','6vWDO969PvNqNYHIOW5v0m','1km0R7wy712AzLkA1WjKET','1h8YIw9HLr6E8gdXVDRbVJ','7lzordPuZEXxwt9aoVZYmG','5IDs1CK15HegSAhGEbSYXo','5M52tdBnJaKSvOpJGz8mfZ','5keeQyPKYRxUCKDMECTXG3','6FBDaR13swtiWwGhX1WQsP','3MM8mtgFzaEJsqbjZBSsHJ','4tpUmLEVLCGFr93o8hFFIB','7MhMgCo0Bl0Kukl93PZbYS','3pTE9iaJTkWns3mxpNQlJV','4LEiUm1SRbFMgfqnQTwUbQ','58lV9VcRSjABbAbfWS6skp','2BWfZGPtsjRlRp7JTDqI45','3eqjTLE0HfPfh78zjh6TqT','0du5cEVh5yTK9QJze8zA0C','3Z02hBLubJxuFJfhacLSDc','5RNFFojXkPRmlJZIwXeKQC','1OmdWpAh1pucAuZPzJaxIJ','7CajNmpbOovFoOoasH2HaY','7JKYaxqsOWhaHjsG9AVJ7y','1anyVhU62p31KFi8MEzkbf','5fScAXreYFnuqwOgBsJgSd','3jNkaOXasoc7RsxdchvEVq','1GhPHrq36VKCY3ucVaZCfo','3Ebn7mKYzD0L3DaUB1gNJZ','4gzpq5DPGxSnKTe4SA8HAU','2Z7gV3uEh1ckIaBzTUCE6R','0vEsuISMWAKNctLlUAhSZC','7ohlPA8dRBtCf92zaZCaaB','2AV6XDIs32ofIJhkkDevjm','4P0dddbxPil35MNN9G2MEX','4tZwfgrHOc3mvqYlEYSvVi','14r9dR01KeBLFfylVSKCZQ','0O98jlCaPzvsoei6U5jfEL','77tT1kLj6mCWtFNqiOmP9H','0oSGxfWSnnOXhD2fKuz2Gy','20vuBdFblWUo2FCOvUzusB','7J2lZBANizgPNfUzux31PV','1Cs0zKBU1kc0i8ypK3B9ai','2CIMQHirSU0MQqyYHq0eOx','6H1RjVyNruCmrBEWRbD0VZ','762310PdDnwsDxAQxzQkfX','0gusqTJKxtU1UTmNRMHZcv','3TVXtAsR1Inumwj472S9r4','0lZoBs4Pzo7R89JM9lxwoT','0fgYKF9Avljex0L9Wt5b8Z','6eUKZXaKkcviH0Ku9w2n3V','0TJB3EE2efClsYIDQ8V2Jk','2BGRfQgtzikz1pzAD0kaEn','7dGJo4pcD2V6oG8kP0tJRR','1uQWmt1OhuHGRKmZ2ZcL6p','6GbCJZrI318Ybm8mY36Of5','5T4UKHhr4HGIC0VzdZQtAE','4Y7tXHSEejGu1vQ9bwDdXW','2kGBy2WHvF0VdZyqiVCkDT','0ZZr6Y49NZWRJc0uCwqpMR','4EVpmkEwrLYEg6jIsiPMIb','08GQAI4eElDnROBrJRGE0X','1moxjboGR7GNWYIMWsRjgG','6FQqZYVfTNQ1pCqfkwVFEa','7jy3rLJdDQY21OgRLCZ9sD','0XNa1vTidXlvJ2gHSsRi4A','3mZqziCJj4pq3P2VBpmK6p','4AbDWrmJPSOeIbT2Ou60ik','6S0GHTqz5sxK5f9HtLXn9q','6V6WCgi7waF55bJmylC4H5','5BKsn7SCN2XmbF7apdCpRS','3AA28KZvwAUcZuOKwyblJQ','2f9ZiYA2ic1r1voObUimdd','3W4xM5XYtUp4ifYYPVKVdk','7oPftvlwr6VrsViSDV7fJY','2Jv5eshHtLycR6R8KQCdc4','67tgMwUfnmqzYsNAtnP6YJ','3qm84nBOXUEQ2vnTfUTTFC','339DNkQkuhHKEcHw6oK8f0','2jK54ZlZhTF1TxygsVeR05','6IDifUtaIPK4yuAiq5W2iG','37uLId6Z5ZXCx19vuruvv5','3WaJSfKnzc65VDgmj2zU8B','6mdiAmATAx73kdxrNrnlao','5lkiCO9UQ8B23dZ1o0UV4m','4EzkuveR9pLvDVFNx6foYD','7KMqksf0UMdyA0UCf4R3ux','3LpLGlgRS1IKPPwElnpW35','3XxxEq6BREC57nCWXbQZ7o','6J7biCazzYhU3gM9j1wfid','3nFkdlSjzX9mRTtwJOzDYB','1OwarW4LEHnoep20ixRA0y','4gn6f5jaOO75s0oF7ozqGG','3pFCERyEiP5xeN2EsPXhjI','6eLbRJP12OhyvUv4ntto4e','6igfLpd8s6DBBAuwebRUuo','1uNFoZAHBGtllmzznpCI3s','31TPClRtHm23RisEBtV3X7','0LbLWjaweRbO4FDKYlbfNt','5K4W6rqBFWDnAN6FQUkS6x','11wRdbnoYqRddKBrpHt4Ue','7K4k5g1ie2qHIH42UMNO7n','53A0W3U0s8diEn9RhXQhVz','73a6pNH4YtLNgDbPQwXveo','5dKj3B0vI9B2sYxJx9Yfvz','2qk9voo8llSGYcZ6xrBzKx','2h93pZq0e7k5yf4dywlkpM','07XSN3sPlIlB2L2XNcTwJw','1ajKVVeguChWXvyDr7L8rv','3VNITwohbvU5Wuy5PC6dsI','0dmPX6ovclgOy8WWJaFEUU','23fqKkggKUBHNkbKtXEls4','2Lhs0asnFQiLuntn3s8p78','066X20Nz7iquqkkCW6Jxy6','72hqBMsw7x5jnfxxwkii8L','5gznATMVO85ZcLTkE9ULU7','0L9xkvBPcEp1nrhDrodxc5','13saZpZnCDWOI9D4IJhp1f','6XyY86QOPPrYVGvF9ch6wz','7KnaZr690xW0sCihF9Z8oP','60ht0hWRy1yjUDfNsLuHuP','3lcbKPLl0ci2mKRdcP5Etf','0QJIPDAEDILuo8AIq3pMuU','3Sz7ZnJQBIHsXLUSo0OQtM','738wLrAtLtCtFOLvQBXOXp','2uH0RyPcX7fnCcT90HFDQX','6wH6iStAh4KIaWfuhf0NYM','6FXMGgJwohJLUSr5nVlf9X','77oD8X9qLXZhpbCjv53l5n','2ye2Wgw4gimLv2eAKyk1NB','2N4isf5pypyuDVpBofqEN8','3OsRAKCvk37zwYcnzRf5XF','1yAwtBaoHLEDWAnWR87hBT','34UhPkLbtFKRq3nmfFgejG','3iTsJGG39nMg9YiolUgLMQ','3gd8FJtBJtkRxdfbTu19U2','12Chz98pHFMPJEknJQMWvI','7FBcuc1gsnv6Y1nwFtNRCb','5YjEVrNMrIRw2xGbjTN6Ti','20qISvAhX20dpIbOOzGK3q','6v8FB84lnmJs434UJf2Mrm','0yNLKJebCb8Aueb54LYya3','0pf1lcBxh6HiiHQAIzhTI5','4UXJsSlnKd7ltsrHebV79Q','0hCNtLu0JehylgoiP8L4Gh','7sjttK1WcZeyLPn3IsQ62L','0UTbeMH3r0QJB50wYA4VTE','2DaxqgrOhkeH0fpeiQq2f4','7wJ9NwdRWtN92NunmXuwBk','7x5rK9BClDQ8wmCkYAGsQp','4STHEaNw4mPZ2tzheohgXB','2CvCyf1gEVhI0mX6aFXmVI','7Lf3LOZp3U3u2f6cWMd3AH','1w5Kfo2jwwIPruYS2UWh56','2ycnb8Er79LoH2AsR5ldjh','7C4sUpWGlTy7IANjruj02I','5psTfOBPmc8UquYcnS22KE','6zvul52xwTWzilBZl6BUbT','7qlh1IM1XMeQXA9ukp59au','6liAMWkVf5LH7YR9yfFy1Y','3wury2nd8idV4GecUg5xze','0O0lrN34wrcuBenkqlEDZe','36E7oYfz3LLRto6l2WmDcD','1dfeR4HaWDbWqFHLkxsg1d','4pejUc4iciQfgdX6OKulQn','4Z8W4fKeB5YxbusRsdQVPb','2d0hyoQ5ynDBnkvAbJKORj','6wWVKhxIU2cEi0K81v7HvP','450iujbtN6XgiA9pv6fVZz','0L8ExT028jH3ddEcZwqJJ5','4KWTAlx2RvbpseOGMEmROg','1HGTHrRQkw0BtevSo1jucU','5pKCCKE2ajJHZ9KAiaK11H','1OwarW4LEHnoep20ixRA0y','2y8Jo9CKhJvtfeKOsYzRdT','3lHXm91pKLq9Sxi6CoRKWu','3fhOTtm0LBJ3Ojn4hIljLo','4WN5naL3ofxrVBgFpguzKo','3CQIn7N5CuRDP8wEI7FiDA','2qc41rNTtdLK0tV3mJn2Pm','3Y10boYzeuFCJ4Qgp53w6o','2wpJOPmf1TIOzrB9mzHifd','5GtMEZEeFFsuHY8ad4kOxv','6OVkHZQP8QoBYqr1ejCGDv','7ooOn6bokl4mGV4CEaUz6A','6UUrUCIZtQeOf8tC0WuzRy','6hN9F0iuULZYWXppob22Aj','4sD9znwiVFx9cgRPZ42aQ1','2p1fiYHYiXz9qi0JJyxBzN','5HlXA01kcjssYDT7EoqUJF','05fG473iIaoy82BF1aGhL8','5m8H6zSadhu1j9Yi04VLqD','7hJcb9fa4alzcOq3EaNPoG','3rIZMv9rysU7JkLzEaC5Jp','2sIx6SmAMw9IBySG3Uj0jf','6Jrj26oAY96EEC2lqC6fua','7bcbShaqKdcyjnmv4Ix8j6','4gIdjgLlvgEOz7MexDZzpM','21UJ7PRWb3Etgsu99f8yo8','2UBTfUoLI07iRqGeUrwhZh','7guDJrEfX3qb6FEbdPA5qi','6PHIK3kjWggLtVygsOtpqS','4MXUO7sVCaFgFjoTI5ox5c','7rZNSLWMjTbwdLNskFbzFf','0FOcXqJgJ1oq9XfzYTDZmZ','3X0tJzVYoWlfjLYI0Ridsw','5eAWCfyUhZtHHtBdNk56l1','3dBVyJ7JuOMt4GE9607Qin','5INjqkS1o8h1imAzPqGZBb','5JsdVATHNPE0XdMFMRoSuf','3mIj9lX2MWuHmhNCA7LSCW','3gdbcIdNypBsYNu3iiCjtN','5krkohEVJYw0qoB5VWwxaC','1yxSLGMDHlW21z4YXirZDS','7mnBLXK823vNxN3UWB7Gfz','40oYPr305MsT2lsiXr9fX9','17U2ImH5IyYMvjkCfPhMHT','7bu3H8JO7d0UbMoVzbo70s','5r1bdqzhgRoHC3YcCV6N5a','27pyLBNdWVJBkbykvbf3TW','16eRpMNXSQ15wuJoeqguaB','6iy8nrBbtL57i4eUttHTww','3jc496ljiyrS3ECrD7QiqL','1aX2dmV8XoHYCOQRxjPESG','4PsjwNjuhm45waas7wa1xJ','0C0XlULifJtAgn6ZNCW2eu','1TrwMxRrrlk0hZxJkw4jUF','4fSPtBgFPZzygkY6MehwQ7','0vW8z9pZMGCcRtGPGtyqiB','2cCUtGK9sDU2EoElnk0GNB','5LfGQac0EIXyAN8aUwmNAQ','7FPkZue0zzjHaOPJb4WCw3','2kreKea2n96dXjcyAU9j5N','5NGO30tJxFlKixkPSgXcFE','0GByy3DcfbQwDvXGCWmzv9','4k1ELeJKT1ISyDv8JivPpB','22bE4uQ6baNwSHPVcDxLCe','1u7kkVrr14iBvrpYnZILJR','40Yq4vzPs9VNUrIBG5Jr2i','3yY2gUcIsjMr8hjo51PoJ8','1lYT0A0LV5DUfxr6doRP3d','4GvOygVQquMaPm8oAc0vXi','0epOFNiUfyON9EYx7Tpr6V','4BntNFyiN3VGG4hhRRZt9d','0Ak6DLKHtpR6TEEnmcorKA','2cGwlqi3k18jFpUyTrsR84','6g0mn3tzAds6aVeUYRsryU','1Xyo4u8uXC1ZmMpatF05PJ','4F84IBURUo98rz4r61KF70','67ea9eGLXYMsO2eYQRui3w','0Ya43ZKWHTKkAbkoJJkwIB','2qV7axHq9Jk7QqFcB3f05A','5jVeqi3PNaTOajfvBa4uFn','2ILGhwWQ0X2HH7iJyH0LWW','4tX2TplrkIP4v05BNC903e','0wHrpPuQ3Qea6UXAc06ocM','2yEwvVSSSUkcLeSTNyHKh8','3bUwxJgNakzYKkqAVgZLlh','536BYVgOnRky0xjsPT96zl','51Blml2LZPmy7TTiAg47vQ','69MEO1AADKg1IZrq2XLzo5','5BvJzeQpmsdsFp4HGUYUEx','44NX2ffIYHr6D4n7RaZF7A','162DCkd8aDKwvjBb74Gu8b','2QoU3awHVdcHS8LrZEKvSM','4zrFO6P7G6EZry0pfxMfKT','2U6gqwyl9F33YxawnFrZG7','5hAhrnb0Ch4ODwWu4tsbpi','77zlytAFjPFjUKda8TNIDY','09hVIj6vWgoCDtT03h8ZCa','0Xf8oDAJYd2D0k3NLI19OV','1G9G7WwrXka3Z1r7aIDjI7','1GhPHrq36VKCY3ucVaZCfo','1PXHzxRDiLnjqNrRn2Xbsa','2wIVse2owClT7go1WT98tk','3G3Gdm0ZRAOxLrbyjfhii5','3iOvXCl6edW5Um0fXEBRXy','3PhoLpVuITZKcymswpck5b','3Rsr4Z96O6U3lToOiV3zBh','3vbKDsSS70ZX9D2OcvbZmS','6Q192DXotxtaysaqNPy5yR','7MqnCTCAX6SsIYYdJCQj9B','7w29UYBi0qsHi5RTcv3lmA']
print 'there are ', len(artists), ' artists'
record = {}

for artist in artists:
    print artist
    #Form a URL by combining different parts
    fullurl = baseurl+str(artist)+'?access_token='+token
    print 'scraping', fullurl
    response = urllib.urlopen(fullurl)
    data = json.loads(response.read())
    print data['name']
    print data['genres']
    #create an empty string - we'll then add each genre to turn a list into a single comma separated string
    genres = ''
    for genre in data['genres']:
        genres = genres+','+genre
    record['genres'] = genres[1:]
    record['name'] = data['name']
    record['popularity'] = data['popularity']
    record['type'] = data['type']
    record['followers'] = data['followers']['total']
    record['fullurl'] = fullurl
    record['artistid'] = artist
    #Now grab the top tracks
    tracksurl = baseurl+artist+'/top-tracks?country=GB&access_token='+token
    print 'scraping tracks: ', tracksurl
    response = urllib.urlopen(tracksurl)
    data = json.loads(response.read())
    #for tracks we have the same problem as genres above, so we create 3 empty strings to store the name, id, and popularity
    tracks = ""
    trackpops = ''
    trackids = ''
    for track in data['tracks']:
        print track['name']
        tracks = tracks+','+track['name']
        trackpops = trackpops+','+str(track['popularity'])
        trackids = trackids+','+track['id']
    record['tracks'] = tracks[1:]
    record['trackpops'] = trackpops[1:]
    record['trackids'] = trackids[1:]
    #Now onto related artists
    relatedurl = baseurl+artist+'/related-artists?access_token='+token
    print 'scraping related artists: ', relatedurl
    response = urllib.urlopen(relatedurl)
    data = json.loads(response.read())
    relatedartists = ''
    relatedartistspop = ''
    relatedartistsid = ''
    print data['artists']
    for artist in data['artists']:
        relatedartists = relatedartists+','+artist['name']
        relatedartistspop = relatedartistspop+','+str(artist['popularity'])
        relatedartistsid = relatedartistsid+','+artist['id']
    record['relatedartists'] = relatedartists[1:]
    record['relatedartistspop'] = relatedartistspop[1:]
    record['relatedartistsid'] = relatedartistsid[1:]
    scraperwiki.sqlite.save(['artistid'], record)


