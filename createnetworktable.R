
col1 <- c()
col2 <- c()
for (artist in 1:305){
 for (related in 01:20){
  #print(paste(artists[artist],":", relateds[[artist]][related]))
  col1 <- c(col1,artists[artist])
  col2 <- c(col2,relateds[[artist]][related])
 }
}