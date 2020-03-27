#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node * next;
};
typedef struct node NODE;

NODE * delete_from_start(NODE *start)
{
    if(start == NULL)
    {
        printf("List empty\n");
        return start;
    }

    if(start->next == NULL)
    {
        printf("%d Deleted\n",start->data);
        free(start);
        start = NULL;
        return start;
    }
    NODE * temp = start;
    start = start->next;
    printf("%d Deleted\n",temp->data);
}

NODE * delete_from_end(NODE *start)
{
    if(start == NULL)
    {
        printf("List Empty\n");
        return start;
    }

    if(start->next == NULL)
    {
        printf("%d Deleted\n",start->data);
        free(start);
        return NULL;
    }
    NODE *p = NULL;
    NODE *c = start;

    while(c->next != NULL)
    {
        p = c;
        c = c->next;
    }

    printf("%d Deleted.\n",c->data);
    free(c);
    p->next = NULL;
    return start;
}

void display(NODE * start)
{
    if(start == NULL)
    {
        printf("List Empty\n");
        return;
    }

    NODE * temp = start;
    while(temp!= NULL)
    {
        printf("%d-->",temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

NODE * insert_at_end(NODE *start)
{
    NODE *newnode;
    newnode = malloc(sizeof(NODE));
    if (newnode == NULL)
    {
        printf("Memory Allocation FAILED...\n");
        return start;
    }
    printf("Enter node data\n");
    scanf("%d",&newnode->data);
    newnode->next = NULL;


    if(start == NULL)
    {
        start = newnode;
        return start;
    }
    NODE *temp;
    temp = start;
    while(temp->next != NULL)
        temp = temp->next;

    temp->next = newnode;
    return start;


}
NODE *insert_at_start(NODE *start)
{
    NODE *newnode;
    newnode = malloc(sizeof(NODE));
    if(newnode == NULL)
    {
        printf("Memory Allocation FAILED...\n");
        return start;
    }
    printf("Enter node data\n");
    scanf("%d",&newnode->data);
    newnode->next = NULL;


    if(start == NULL)
    {
        start = newnode;
        return start;
    }
    newnode->next = start;
    start = newnode;
    return start;

    /*
    if(start!=NULL)
    {
    newnode->next = start;
    return start;
    */
}



int main()
{
    NODE *start = NULL;

    int choice;
    while(1)
    {
        printf("** MENU **\n1-Insert at start\n2-Insert at end\n3-Delete from start\n4-Delete from end\n5-Display List\n6-Exit\n******************\n");
        printf("Enter your choice\n");
        scanf("%d",&choice);

        switch(choice)
        {
            case 1: start = insert_at_start(start);
                    break;
            case 2: start = insert_at_end(start);
                    break;
            case 3: start = delete_from_start(start);
                    break;
            case 4: start = delete_from_end(start);
                    break;
            case 5: display(start);
                    break;
            case 6: printf("Terminating............\n");
                    exit(0);

        }
    }
    return 0;
}
