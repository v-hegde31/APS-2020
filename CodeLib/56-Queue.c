#include <stdio.h>
#include <stdlib.h>
#define MAXQUEUE 5
#define TRUE 1
#define FALSE 0

struct queue
{
    int front;
    int rear;
    int items[MAXQUEUE];
};
typedef struct queue QUEUE;

int empty(QUEUE *q)
{
    if(q->front>q->rear)
        return TRUE;
    else
        return FALSE;
}

int full(QUEUE *q)
{
    if(q->rear==MAXQUEUE-1)
        return TRUE;
    else
        return FALSE;
}

void enqueue(QUEUE *q)
{
    if(full(q))
    {
        printf("QUEUE FULL\n");
        return;
    }

    int x;
    printf("Enter item to enqueue:\n");
    scanf("%d",&x);
    q->rear++;
    q->items[q->rear]=x;
    printf("Enqueue Success.\n");
    return;
}

void dequeue(QUEUE *q)
{
    if(empty(q))
    {
        printf("Queue empty\n");
        return;
    }
    int x;
    x = q->items[q->front];
    q->front++;
    printf("Dequeued element: %d\n",x);
}

void display(QUEUE *q)
{
    int i;
    for(i=q->front;i<=q->rear;i++)
    {
        printf("|%d|\n",q->items);
    }

}
int main()
{
    QUEUE q;
    q.front = 0;
    q.rear = -1;
    int choice =0;
    while(1)
    {
        printf("Menu\n 1-Enqueue/2-Dequeue/3-Display/4-Exit\n*******\n");
        printf("Enter Your Choice\n");
        scanf("%d",&choice);

        switch(choice)
        {
            case 1: enqueue(&q);
                    break;
            case 2: dequeue(&q);
                    break;
            case 3: display(&q);
                    break;
            case 4: printf("Terminating....\n");
                    exit(0);
        }
    }
    return 0;
}
