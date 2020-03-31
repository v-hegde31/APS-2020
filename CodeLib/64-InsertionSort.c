int i,j,key,count=0;
	for(i=1;i<n;i++)
	{
		key=a[i];
		j=i-1;
		while(j>-1 && a[j]>key)
		{
			count++;
			a[j+1]=a[j];
			j--;
		}
		a[j+1]=key;
	}
