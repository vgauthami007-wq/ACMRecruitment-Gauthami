let us picturise the given sudoko 

let a cell in the sudoko be named [x,y] where x is row number and y is coloumn number
in the cell [1,1] the number will be 1 since [1,2] an [1,4] cannot be 1 and there should be 1 in the row
now in the cell [3,3] the number will be 1 for the same reason
in the cell [4,4] the nubmer will be 3 since the 3 cannot be in the rest of the row
since we have completed 1 and 3 in every row now we need to fill the squares with 2 and 4
we can fill 1 row with 2 and 4 anyway because there isn't any restriction
so i completed the first row by filling cell [1,2] and [1,4] with 2 and 4 respectively
in row3 2 cannot be filled in sqaure[3,2] since there is already a 2 in the given coloumn so we need to fill the cell [3,4] with 2 and compplete the row by filling [3,2] with 4
now we are left with 2 rows, we can first complete one row by inserting 2 and 4 anywhere in the given row as there is no restriction 
i filled cell [2,1] and [2,3] with 2 and 4 respectively
now this leaves us with row4, since [4,1]  cannot be filled with 2 since there is 2 in the given coloumn so we fill cell [4,3] with 2 instead and complete the row by filling [4,1] cell with 4

