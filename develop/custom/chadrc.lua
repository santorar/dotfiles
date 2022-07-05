-- Just an example, supposed to be placed in /lua/custom/

local M = {}

-- make sure you maintain the structure of `core/default_config.lua` here,
-- example of changing theme:

M.ui = {
   theme = "gruvbox",
}
M.plugins = {
   user = require "custom.plugins",
   options = {
      lspconfig = {
         setup_lspconf = "custom.plugins.lspconfig",
      },
   },
   override = {
      ["nvim-treesitter/nvim-treesitter"] = {
         ensure_installed = {
            "html",
            "css",
            "javascript",
            "python",
         },
      },
   },
}

return M
