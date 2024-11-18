const express = require("express");

const createServer = (pool, port = 3000) => {
  const app = express();

  // Helper function to organize comments into a tree structure
  const organizeComments = (comments) => {
    const map = new Map();
    const result = [];

    // Step 1: Populate the map with comments, initializing 'children' as an empty array.
    comments.forEach((comment) => {
      map.set(comment.id, { ...comment, children: [] });
    });

    // Step 2: Organize the comments, adding children to their respective parents.
    comments.forEach((comment) => {
      if (comment.parent_id) {
        // Add child to the parent
        map.get(comment.parent_id).children.push(map.get(comment.id));
      } else {
        // For top-level comments (no parent_id), add to the result
        result.push(map.get(comment.id));
      }
    });

    return result;
  };

  // Route to fetch comments for a post
  app.get("/posts/:id/comments", async (req, res) => {
    const postId = req.params.id;

    try {
      // Query to get all comments for the given post
      const result = await pool.query(
        'SELECT * FROM comments WHERE post_id = $1 ORDER BY id',
        [postId]
      );

      // If no comments exist for this post, return 404
      if (result.rows.length === 0) {
        return res.status(404).json({ message: "No comments found for this post" });
      }

      // Organize the comments into a tree structure
      const organizedComments = organizeComments(result.rows);

      // Send the response with organized comments
      res.status(200).json({ data: organizedComments });
    } catch (error) {
      console.error('Error fetching comments:', error);
      res.status(500).json({ message: "Internal server error" });
    }
  });

  const server = app.listen(port, () =>
    console.log(`[server] listening on port ${port}`)
  );
  return {
    app,
    close: () => new Promise(resolve => {
      server.close(() => {
        resolve();
        console.log("[server] closed");
      });
    }),
  };
};

module.exports = { createServer };
