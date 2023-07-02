#include<iostream>
using namespace std;
 
 struct node{
	int val;
	node *next;
}*ptr=NULL,*tmp=NULL,*head=NULL;

void insert(int x)
{
	tmp=new node();
	tmp->val=x;
	tmp->next=NULL;
	
	if(head==NULL)
	{
		head=ptr=tmp;
	}
	else
	{
		ptr->next=tmp;
		ptr=tmp;
	}
}

void insert_pos(int x,int pos)
{	

	int i=0;
	node *n;
	n=head;
	tmp=new node();
	tmp->val=x;
	while(i<=pos)
		{
	
		if(i==pos)
			{ n->next=tmp;
			tmp->next=n->next->next;
			
				}
		n=n->next;
		i++;
		
		}
}

void disply()
{
	node *m;
	m=head;
	while(m->next!=NULL)
	{
		cout<<m->val<<"->";
		m=m->next;
	}
}

int main()
{
	int ch,x;
	int y,pos;
	do{
	
	cout<<"enter your choice";
	cin>>ch;
	int b;
	switch(ch)
	{
		
		case 1:cout<<"enter for number\n";
			cin>>x;
			  insert(x);
			  break;
			  
				
		case 2:disply();
			break;
			
		case 3:cout<<"enter position\n";
			cin>>pos;
			cout<<"entert the value";
			cin>>y;
			insert_pos(y,pos);
			break;			  			
	}
	}while(ch<=3);
}