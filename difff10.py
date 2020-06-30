L1=[1,3,5,7,9]
L2=[1,2,4,6,7,8]
diff_L1_L2=list(set(L1)-set(L2))
diff_L2_L1=list(set(L2)-set(L1))
total_diff=diff_L1_L2+diff_L2_L1
print(total_diff)
