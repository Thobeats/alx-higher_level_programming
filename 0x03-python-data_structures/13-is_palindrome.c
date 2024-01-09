#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: The head of the singly linked list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		listint_t *temp = slow->next;

		slow->next = prev_slow;
		prev_slow = slow;
		slow = temp;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	while (prev_slow != NULL && slow != NULL)
	{
		if (prev_slow->n != slow->n)
		{
			return (0);
		}
		prev_slow = prev_slow->next;
		slow = slow->next;
	}
	return (1);
}
