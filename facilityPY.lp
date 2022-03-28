\ Model facility
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
 [ 0.4 open[6] * utilization_rate[60] + 0.4 open[6] * utilization_rate[62]
   + 0.2 open[6] * utilization_rate[66]
   + 0.4 open[6] * utilization_rate[69]
   + 0.1666666666666667 open[7] * utilization_rate[70]
   + 0.2083333333333333 open[7] * utilization_rate[71]
   + 0.1666666666666667 open[7] * utilization_rate[72]
   + 0.2083333333333333 open[7] * utilization_rate[74]
   + 0.0833333333333333 open[7] * utilization_rate[76]
   + 0.625 open[7] * utilization_rate[77]
   + 0.4166666666666667 open[7] * utilization_rate[78]
   + 0.1666666666666667 open[7] * utilization_rate[79] ] / 2 
Subject To
 R0: utilization_rate[0] + utilization_rate[10] + utilization_rate[20]
   + utilization_rate[30] + utilization_rate[40] + utilization_rate[50]
   + utilization_rate[60] + utilization_rate[70] + utilization_rate[80]
   + utilization_rate[90] = 1
 R1: utilization_rate[1] + utilization_rate[11] + utilization_rate[21]
   + utilization_rate[31] + utilization_rate[41] + utilization_rate[51]
   + utilization_rate[61] + utilization_rate[71] + utilization_rate[81]
   + utilization_rate[91] = 1
 R2: utilization_rate[2] + utilization_rate[12] + utilization_rate[22]
   + utilization_rate[32] + utilization_rate[42] + utilization_rate[52]
   + utilization_rate[62] + utilization_rate[72] + utilization_rate[82]
   + utilization_rate[92] = 1
 R3: utilization_rate[3] + utilization_rate[13] + utilization_rate[23]
   + utilization_rate[33] + utilization_rate[43] + utilization_rate[53]
   + utilization_rate[63] + utilization_rate[73] + utilization_rate[83]
   + utilization_rate[93] = 1
 R4: utilization_rate[4] + utilization_rate[14] + utilization_rate[24]
   + utilization_rate[34] + utilization_rate[44] + utilization_rate[54]
   + utilization_rate[64] + utilization_rate[74] + utilization_rate[84]
   + utilization_rate[94] = 1
 R5: utilization_rate[5] + utilization_rate[15] + utilization_rate[25]
   + utilization_rate[35] + utilization_rate[45] + utilization_rate[55]
   + utilization_rate[65] + utilization_rate[75] + utilization_rate[85]
   + utilization_rate[95] = 1
 R6: utilization_rate[6] + utilization_rate[16] + utilization_rate[26]
   + utilization_rate[36] + utilization_rate[46] + utilization_rate[56]
   + utilization_rate[66] + utilization_rate[76] + utilization_rate[86]
   + utilization_rate[96] = 1
 R7: utilization_rate[7] + utilization_rate[17] + utilization_rate[27]
   + utilization_rate[37] + utilization_rate[47] + utilization_rate[57]
   + utilization_rate[67] + utilization_rate[77] + utilization_rate[87]
   + utilization_rate[97] = 1
 R8: utilization_rate[8] + utilization_rate[18] + utilization_rate[28]
   + utilization_rate[38] + utilization_rate[48] + utilization_rate[58]
   + utilization_rate[68] + utilization_rate[78] + utilization_rate[88]
   + utilization_rate[98] = 1
 R9: utilization_rate[9] + utilization_rate[19] + utilization_rate[29]
   + utilization_rate[39] + utilization_rate[49] + utilization_rate[59]
   + utilization_rate[69] + utilization_rate[79] + utilization_rate[89]
   + utilization_rate[99] = 1
 R10: open[0] + open[1] + open[2] + open[3] + open[4] + open[5] + open[6]
   + open[7] + open[8] + open[9] <= 2
Bounds
Binaries
 open[0] open[1] open[2] open[3] open[4] open[5] open[6] open[7] open[8]
 open[9] utilization_rate[0] utilization_rate[1] utilization_rate[2]
 utilization_rate[3] utilization_rate[4] utilization_rate[5]
 utilization_rate[6] utilization_rate[7] utilization_rate[8]
 utilization_rate[9] utilization_rate[10] utilization_rate[11]
 utilization_rate[12] utilization_rate[13] utilization_rate[14]
 utilization_rate[15] utilization_rate[16] utilization_rate[17]
 utilization_rate[18] utilization_rate[19] utilization_rate[20]
 utilization_rate[21] utilization_rate[22] utilization_rate[23]
 utilization_rate[24] utilization_rate[25] utilization_rate[26]
 utilization_rate[27] utilization_rate[28] utilization_rate[29]
 utilization_rate[30] utilization_rate[31] utilization_rate[32]
 utilization_rate[33] utilization_rate[34] utilization_rate[35]
 utilization_rate[36] utilization_rate[37] utilization_rate[38]
 utilization_rate[39] utilization_rate[40] utilization_rate[41]
 utilization_rate[42] utilization_rate[43] utilization_rate[44]
 utilization_rate[45] utilization_rate[46] utilization_rate[47]
 utilization_rate[48] utilization_rate[49] utilization_rate[50]
 utilization_rate[51] utilization_rate[52] utilization_rate[53]
 utilization_rate[54] utilization_rate[55] utilization_rate[56]
 utilization_rate[57] utilization_rate[58] utilization_rate[59]
 utilization_rate[60] utilization_rate[61] utilization_rate[62]
 utilization_rate[63] utilization_rate[64] utilization_rate[65]
 utilization_rate[66] utilization_rate[67] utilization_rate[68]
 utilization_rate[69] utilization_rate[70] utilization_rate[71]
 utilization_rate[72] utilization_rate[73] utilization_rate[74]
 utilization_rate[75] utilization_rate[76] utilization_rate[77]
 utilization_rate[78] utilization_rate[79] utilization_rate[80]
 utilization_rate[81] utilization_rate[82] utilization_rate[83]
 utilization_rate[84] utilization_rate[85] utilization_rate[86]
 utilization_rate[87] utilization_rate[88] utilization_rate[89]
 utilization_rate[90] utilization_rate[91] utilization_rate[92]
 utilization_rate[93] utilization_rate[94] utilization_rate[95]
 utilization_rate[96] utilization_rate[97] utilization_rate[98]
 utilization_rate[99]
End
