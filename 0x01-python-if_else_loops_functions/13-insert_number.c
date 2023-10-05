#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert number in a sorted list
 * @head: linked list head
 * @number: inserted number
 * Return: ptr to new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nd = *head;
	listint_t *new_nd = malloc(sizeof(listint_t));

	if (!new_nd)
		return (NULL);
	new_nd->n = number;
	new_nd->next = NULL;

	if (new_nd->n < nd->n || !nd)
	{
		new_nd->next = nd;
		*head = new_nd;
		return (new_nd);
	}

	while (nd)
	{
		if (new_nd->n < nd->next->n || !nd->next)
		{
			new_nd->next = nd->next;
			nd->next = new_nd;
			return (new_nd);
		}
		nd = nd->next;
	}

	return (NULL);
}
