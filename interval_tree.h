#ifndef INTERVALTREE_H
#define INTERVALTREE_H

using namespace std;

class interval_tree
{
public:
	struct Interval;
	struct ITNode;
	ITNode * newNode(Interval i);
	ITNode *insert(ITNode *root, Interval i);
	bool doOVerlap(Interval i1, Interval i2);
	Interval *overlapSearch(ITNode *root, Interval i);
	void inorder(ITNode *root);
	int main();
};

#endif