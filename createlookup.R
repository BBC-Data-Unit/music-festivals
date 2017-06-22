relateds <- spotifydata$relatedartists
relatedids <- spotifydata$relatedartistsid
relatedpops <- spotifydata$relatedartistspop
colid <- c()
colname <- c()
colpop <- c()
for (artist in 1:305){
 for (related in 01:20){
  #print(paste(artists[artist],":", relateds[[artist]][related]))
   colid <- c(colid,relatedids[[artist]][related])
   colname <- c(colname,relateds[[artist]][related])
   colpop <- c(colpop,relatedpops[[artist]][related])
 }
}