#include "lists.h"

/**
 * insert_node - a function that inserts a number into a sorted singly linked list
 * @head: a pointer to the head of linked list
 * @number: the number we want to insert
 * Return: a pointer to the updated linked list
*/

listint_t *insert_node(listint_t **head, int number)
{
	/*listint_t *current = malloc(sizeof(listint_t));*/
	listint_t *current = *head;
	/*listint_t *new_list = malloc(sizeof(listint_t));*/
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *check = *head;

	if (!new)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (*head);
	}

	while (new->n > check->n)
	{
		/*Keep track of the value the current node*/
		current = check;
		check = check->next;
	}
	current->next = new;
	new->next = check;
	
	return (*head);
}
