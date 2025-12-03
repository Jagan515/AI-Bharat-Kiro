/**
 * Binary Tree Traversal - Inorder, Preorder, Postorder
 */
import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    
    TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

public class TreeTraversal {
    // Inorder traversal: Left -> Root -> Right
    public void inorderTraversal(TreeNode root) {
        if (root == null) return;
        
        inorderTraversal(root.left);
        System.out.print(root.val + " ");
        inorderTraversal(root.right);
    }
    
    // Preorder traversal: Root -> Left -> Right
    public void preorderTraversal(TreeNode root) {
        if (root == null) return;
        
        System.out.print(root.val + " ");
        preorderTraversal(root.left);
        preorderTraversal(root.right);
    }
    
    // Postorder traversal: Left -> Right -> Root
    public void postorderTraversal(TreeNode root) {
        if (root == null) return;
        
        postorderTraversal(root.left);
        postorderTraversal(root.right);
        System.out.print(root.val + " ");
    }
    
    public static void main(String[] args) {
        TreeTraversal tree = new TreeTraversal();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        
        System.out.println("Inorder traversal:");
        tree.inorderTraversal(root);
        
        System.out.println("\nPreorder traversal:");
        tree.preorderTraversal(root);
        
        System.out.println("\nPostorder traversal:");
        tree.postorderTraversal(root);
    }
}
