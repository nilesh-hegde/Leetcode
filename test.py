nums=[-1,0,1,2,-1,-4]
threesum=[]
nums.sort()
i=0
while i<=len(nums)-3:
	if nums[i]>0:
		break
	if i>0 and nums[i]==nums[i-1]:
		continue
	i=i+1
	h=len(nums)-1
	l=i+1
	while l<h:
		if l>i and nums[l]==nums[l-1]:
			l=l+1
			continue
		if h<len(nums)-1 and nums[h]==nums[h+1]:
			h=h-1
			continue
		if nums[i]+nums[l]+nums[h]<0:
			l=l+1
			continue
		if nums[i]+nums[l]+nums[h]>0:
			h=h-1
			continue
		threesum.append([nums[i],nums[l],nums[h]])
		l=l+1
		h=h-1
	i=i+1
print(threesum)