#include <stdio.h>
#include <stdlib.h>
struct tree
{
    int data;
    struct tree *left;
    struct tree *right;
};
typedef struct tree TREE;

static int count=0;
static int leaf_count=0;
static int search_count=0;
static int edge = 0;

TREE *insert_into_bst(TREE *root)
{
    TREE *newnode;

    newnode = (TREE *)malloc(sizeof(TREE));
    if(newnode == NULL)
    {
        printf("Memory allocation failed\n");
        return root;
    }

    printf("Enter data to be inserted\n");
    scanf("%d",&newnode->data);
    newnode->left = NULL;
    newnode->right = NULL;

    if(root == NULL)
    {
        root = newnode;
        printf("Root created\n");
        return root;
    }

    TREE *prev, *curr;
    prev = NULL;
    curr = root;

    while(curr != NULL)
    {
        prev = curr;
        if(newnode->data < curr->data)
            curr = curr->left;
        else
            curr = curr->right;
    }

    if(newnode->data < prev->data)
        prev->left = newnode;
    else
        prev->right = newnode;
    printf("node attached to BST\n");
    return root;
}

void inorder(TREE *root)
{
    if(root != NULL)
    {
        inorder(root->left);
        printf("%d\t",root->data);
        inorder(root->right);
    }
}

void preorder(TREE *root)
{
    if(root != NULL)
    {
        printf("%d\t",root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

void postorder(TREE *root)
{
    if(root != NULL)
    {
        postorder(root->left);
        postorder(root->right);
        printf("%d\t",root->data);
    }
}

int edges(TREE *root)
{
    if(root !=NULL)
    {
        edges(root->right);
        edge++;
    }
    return edge;
}

int counter(TREE *root)
{
    if(root != NULL)
    {
        counter(root->left);
        count++;
        counter(root->right);
    }
    return count;
}

int leafcount(TREE *root)
{
    if(root != NULL)
    {
        leafcount(root->left);
        if(root->left == NULL && root->right == NULL)
            leaf_count++;
        leafcount(root->right);
    }
    return leaf_count;
}

int searchcount(TREE *root, int k)
{
    if(root != NULL)
    {
        searchcount(root->left,k);
        if(root->data > k)
            search_count++;
        searchcount(root->right,k);
    }
    return search_count;
}

int levelone(TREE *root)
{
    if(root==NULL)
        return 0;
    if(root->left==NULL && root->right==NULL)
        return 0;
    if(root->left==NULL || root->right==NULL)
        return 1;
    else
        return 2;
}

void min_item(TREE *root)
{
    TREE *prev, *curr;
    prev=NULL;
    curr=root;

    while(root!=NULL)
    {

    }

}

TREE * delete_from_bst(TREE * root, int item)
{
    TREE * currnode, *parent, *successor, *p;

    if(root == NULL)
    {
        printf("Tree is empty\n");
        return root;
    }

    parent = NULL;
    currnode = root;

    while((currnode != NULL) && (item != currnode->data))
    {
        parent = currnode;
        if(item < currnode->data)
            currnode  = currnode->left;
        else
            currnode = currnode->right;
    }

    if(currnode == NULL)  {
        printf("Item not found\n");
        return root;
    }

    if(currnode->left == NULL)
        p = currnode->right;
    else if (currnode->right == NULL)
        p = currnode->left;
    else
    {
        successor = currnode->right;
        while(successor->left != NULL)
            successor = successor->left;

        successor->left = currnode->left;
        p = currnode->right;
    }

    if (parent == NULL) {
        free(currnode);
        return p;
    }

    if(currnode == parent ->left)
        parent->left = p;
    else
        parent->right = p;
    free(currnode);
    return root;
}
int main()
{
    TREE *root = NULL;
    int choice;
    int item,k;
    int nodenumber,leafnumber,searchnumber,levelone,largest;

    while(1)
    {
        printf("\nMENU:\n");
        printf("1-INSERT INTO BST\n2-INORDER TRAVERSAL\n3-PREORDER TRAVERSAL\n4-POSTORDER TRAVERSAL\n5-DELETE NODE\n6-TREE ADDRESS\n7-TOTAL NUMBER OF NODES\n");
        printf("8-LEAF NODE COUNT\n9-NUMBER OF EDGES\n10-COUNT OF NODES THAT HOLD VALUE GREATER THAN K\n11-CHECK IF STRICTLY BINARY\n");
        printf("12-NUMBER OF INTERNAL NODES\n13-NODES AT LEVEL 1\n14-OUT DEGREE OF ROOT NODE\n15-EDGES BETWEEN ROOT NODE AND LARGEST ELEMENT\n0-EXIT\n");
        printf("Enter choice:\t");
        scanf("%d",&choice);

        switch(choice)
        {
            case 0: printf("Terminating....\n");
                    exit(1);
            case 1: root = insert_into_bst(root);
                    break;
            case 2: inorder(root);
                    break;
            case 3: preorder(root);
                    break;
            case 4: postorder(root);
                    break;
            case 5: printf("Enter item to be deleted\n");
                    scanf("%d",&item);
                    root = delete_from_bst(root,item);
                    break;
            case 6: printf("Address of root: %p\n",root);
                    break;
            case 7: nodenumber = counter(root);
                    printf("Number of nodes = %d\n",nodenumber);
                    count=0;
                    break;
            case 8: leafnumber = leafcount(root);
                    printf("Number of leaf nodes = %d\n",leafnumber);
                    leaf_count=0;
                    break;
            case 9: nodenumber = counter(root);
                    printf("Number of edges = %d\n",nodenumber-1);
                    count=0;
                    break;
            case 10:printf("Enter value to be searched:\t");
                    scanf("%d",&k);
                    searchnumber = searchcount(root,k);
                    printf("Number of nodes with data greater than %d = %d",k,searchnumber);
                    break;
            case 11:nodenumber = counter(root);
                    if(nodenumber&1)
                        printf("Given tree is strictly binary\n");
                    else
                        printf("Not strictly binary\n");
                    count=0;
                    break;
            case 12:nodenumber = counter(root);
                    leafnumber = leafcount(root);
                    printf("Number of internal nodes = %d",nodenumber-leafnumber);
                    count=0;
                    leaf_count=0;
                    break;
            case 13:levelone = level_one(root);
                    printf("Number of nodes at level one = %d\n",levelone);
                    break;
            case 14:levelone = level_one(root);
                    printf("Number of nodes at level one = %d\n",levelone);
                    break;
            case 15:largest=edges(root);
                    printf("Number of edges between root and largest element = %d",largest);
                    break;
            case 16:min_item(root);
                    break;
            case 17:max_item(root);
                    break;

        }
    }
    return 0;
}
