int getHeight(Node* root) {
    if (!root) {
        return 0;
    }
    return root->height;
}

int getBalance(Node* root) {
    if (!root) {
        return 0;
    }
    return getHeight(root->left) - getHeight(root->right);
}
Node* leftRotate(Node* z) {
    Node* y = z->right;
    Node* T2 = y->left;
    y->left = z;
    z->right = T2;
    z->height = 1 + max(getHeight(z->left),
                        getHeight(z->right));
    y->height = 1 + max(getHeight(y->left),
                        getHeight(y->right));
    return y;
}

Node* rightRotate(Node* z) {
    Node* y = z->left;
    Node* T3 = y->right;
    y->right = z;
    z->left = T3;
    z->height = 1 + max(getHeight(z->left),
                        getHeight(z->right));
    y->height = 1 + max(getHeight(y->left),
                        getHeight(y->right));
    return y;
}

Node* getMinValueNode(Node* root) {
    if (root == nullptr || root->left == nullptr) {
        return root;
    }
    return getMinValueNode(root->left);
}
Node* deleteNode(Node* root, int key) {
    if (!root) {
        return root;
    } else if (key < root->data) {
        root->left = deleteNode(root->left, key);
    } else if (key > root->data) {
        root->right = deleteNode(root->right, key);
    } else {
        if (root->left == nullptr) {
            Node* temp = root->right;
            delete root;
            return temp;
        } else if (root->right == nullptr) {
            Node* temp = root->left;
            delete root;
            return temp;
        }
        Node* temp = getMinValueNode(root->right);
        root->data = temp->data;
        root->right = deleteNode(root->right, temp->data);
    }
    if (root == nullptr) {
        return root;
    }
    root->height = 1 + max(getHeight(root->left), getHeight(root->right));
    int balance = getBalance(root);
    if (balance > 1 && getBalance(root->left) >= 0) {
        return rightRotate(root);
    }
    if (balance < -1 && getBalance(root->right) <= 0) {
        return leftRotate(root);
    }
    if (balance > 1 && getBalance(root->left) < 0) {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }
    if (balance < -1 && getBalance(root->right) > 0) {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }
    return root;
}
