#include "lists.h"

/**
 * insert_node - function to insert new node in a sorted linked list
 * @head: input pointer to head pointer of singly linked list
 * @number: input number to sort and insert into list as new node
 * Return: pointer to newly added node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t)), *head2, *check;

	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;

	if (head == NULL)
	{
		head = &newnode;
		return (newnode);
	}
	if (*head == NULL)
	{
		(*head) = newnode;
		return (newnode);
	}
	if ((*head)->n >= number)
	{
		newnode->next = (*head);
		(*head) = newnode;
		return (newnode);
	}
	head2 = (*head);
	check = (*head);
	while (check->next != NULL && check->next->next != NULL)
	{
		check = check->next->next;
		if (check->n < number)
			head2 = check;
		else if (head2->next->n <= number)
		{
			newnode->next = head2->next->next;
			head2->next->next = newnode;
			return (newnode);
		}
		else if (head2->n <= number)
		{
			newnode->next = head2->next;
			head2->next = newnode;
			return (newnode);
		}
	}
	if (check->next == NULL)
	{
		check->next = newnode;
		return (newnode);
	}
	if (check->next->n <= number)
	{
		check->next->next = newnode;
		return (newnode);
	}
	newnode->next = check->next;
	check->next = newnode;
	return (newnode);
}
