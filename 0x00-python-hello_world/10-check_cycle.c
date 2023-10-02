#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if there's cycle in the linked list
 * @list: linked list
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_ls = list;
	listint_t *fast_ls = list;

	while (fast_ls && fast_ls->next)
	{
		slow_ls = slow_ls->next;
		fast_ls = fast_ls->next->next;
		if (fast_ls == slow_ls)
			return (1);
	}
	return (0);
}
