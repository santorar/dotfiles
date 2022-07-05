-- custom plugins
return {
   ["jose-elias-alvarez/null-ls.nvim"] = {
      after = "nvim-lspconfig",
      config = function()
         require("custom.plugins.null-ls").setup()
      end,
   },
   ["jose-elias-alvarez/nvim-lsp-ts-utils"] = {},
   ["goolord/alpha-nvim"] = {
      disable = false,
   },
}
