#include "lists.h"

/**
 * check_cycle - function to check if the singly linked list has a cycle
 * @list: pointer to the header of the list
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *check;

	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);
	check = list;

	while (check->next != NULL && check->next->next != NULL)
	{
		list = list->next;
		check = check->next->next;
		if (list == check)
			return (1);
	}

	return (0);
}
